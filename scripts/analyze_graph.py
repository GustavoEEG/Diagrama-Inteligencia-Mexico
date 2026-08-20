#!/usr/bin/env python3
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRADE_ORDER = {g:i for i,g in enumerate('ABCDEFG')}


def load_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def merge_by_id(base, patch):
    out = {x['id']: x for x in base}
    for x in patch:
        out[x['id']] = x
    return list(out.values())


def load_universe():
    manifest = load_json('data/manifest.json')
    nodes = load_json(manifest['base']['nodes'])
    edges = load_json(manifest['base']['edges'])
    for overlay_path in manifest.get('overlays', []):
        ov = load_json(overlay_path)
        nodes = merge_by_id(nodes, ov.get('nodes', []))
        edges = merge_by_id(edges, ov.get('edges', []))
    return nodes, edges


def build_graph(nodes, edges, max_grade='G'):
    ids = {n['id'] for n in nodes}
    adj = {n: set() for n in ids}
    kept=[]
    for e in edges:
        if GRADE_ORDER.get(e.get('g','G'), 99) <= GRADE_ORDER[max_grade] and e['a'] in ids and e['b'] in ids:
            a,b=e['a'],e['b']
            if a==b: continue
            adj[a].add(b); adj[b].add(a); kept.append(e)
    return adj, kept


def components(adj):
    seen=set(); comps=[]
    for s in adj:
        if s in seen: continue
        q=[s]; seen.add(s); comp=[]
        while q:
            u=q.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        comps.append(comp)
    return sorted(comps, key=len, reverse=True)


def betweenness(adj):
    # Brandes, undirected unweighted; normalized to [0,1]
    nodes=list(adj); cb=dict.fromkeys(nodes,0.0)
    for s in nodes:
        stack=[]; pred={w:[] for w in nodes}; sigma=dict.fromkeys(nodes,0.0); sigma[s]=1.0
        dist=dict.fromkeys(nodes,-1); dist[s]=0
        q=deque([s])
        while q:
            v=q.popleft(); stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    q.append(w); dist[w]=dist[v]+1
                if dist[w] == dist[v]+1:
                    sigma[w]+=sigma[v]; pred[w].append(v)
        delta=dict.fromkeys(nodes,0.0)
        while stack:
            w=stack.pop()
            if sigma[w]:
                for v in pred[w]:
                    delta[v] += (sigma[v]/sigma[w])*(1.0+delta[w])
            if w != s: cb[w]+=delta[w]
    for v in cb: cb[v] /= 2.0
    n=len(nodes)
    scale = 2/((n-1)*(n-2)) if n>2 else 0
    return {k:v*scale for k,v in cb.items()}


def articulation_and_bridges(adj):
    time=0; disc={}; low={}; parent={}; arts=set(); bridges=[]
    def dfs(u):
        nonlocal time
        time+=1; disc[u]=low[u]=time; children=0
        for v in adj[u]:
            if v not in disc:
                parent[v]=u; children+=1; dfs(v); low[u]=min(low[u],low[v])
                if u not in parent and children>1: arts.add(u)
                if u in parent and low[v]>=disc[u]: arts.add(u)
                if low[v]>disc[u]: bridges.append(tuple(sorted((u,v))))
            elif parent.get(u)!=v:
                low[u]=min(low[u],disc[v])
    for u in adj:
        if u not in disc: dfs(u)
    return arts, sorted(set(bridges))


def shortest_path(adj, src, dst):
    if src not in adj or dst not in adj: return None
    q=deque([src]); prev={src:None}
    while q:
        u=q.popleft()
        if u==dst: break
        for v in adj[u]:
            if v not in prev:
                prev[v]=u; q.append(v)
    if dst not in prev: return None
    path=[]; u=dst
    while u is not None: path.append(u); u=prev[u]
    return list(reversed(path))


def analyze(nodes, edges, max_grade):
    labels={n['id']: n.get('label',n['id']).replace('\n',' ') for n in nodes}
    adj, kept=build_graph(nodes,edges,max_grade)
    deg={u:len(vs) for u,vs in adj.items()}
    btw=betweenness(adj)
    arts, bridges=articulation_and_bridges(adj)
    comps=components(adj)
    active={u for u,d in deg.items() if d>0}
    return {
      'max_grade': max_grade,
      'nodes_total': len(nodes), 'active_nodes': len(active), 'edges': len(kept),
      'components': [len(c) for c in comps if any(deg[x] for x in c)],
      'degree_top': [(labels[k],k,v) for k,v in sorted(deg.items(), key=lambda kv:(-kv[1],kv[0]))[:15]],
      'betweenness_top': [(labels[k],k,round(v,6)) for k,v in sorted(btw.items(), key=lambda kv:(-kv[1],kv[0]))[:15]],
      'articulation_points': [(labels[k],k,deg[k],round(btw[k],6)) for k in sorted(arts, key=lambda x:(-btw[x],-deg[x],x))],
      'bridges': [(labels[a],a,labels[b],b) for a,b in bridges],
      'paths': {
        'andy_to_huachicol': shortest_path(adj,'andy','huachicol'),
        'olan_to_huachicol': shortest_path(adj,'olan','huachicol'),
        'portacelis_to_ingemar': shortest_path(adj,'portacelis','ingemar'),
        'olan_to_ingemar': shortest_path(adj,'olan','ingemar'),
      }
    }


def main():
    nodes,edges=load_universe()
    out={'AC':analyze(nodes,edges,'C'),'AG':analyze(nodes,edges,'G')}
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
