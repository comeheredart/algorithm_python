{\rtf1\ansi\ansicpg949\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue-Bold;\f1\fnil\fcharset129 AppleSDGothicNeo-Bold;}
{\colortbl;\red255\green255\blue255;\red220\green161\blue13;}
{\*\expandedcolortbl;;\cssrgb\c89412\c68627\c3922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab560
\pard\pardeftab560\slleading20\partightenfactor0

\f0\b\fs26 \cf2 //DFS
\f1 \'b0\'da\'b4\'d9
\f0 ! 
\f1 \'b1\'ed\'c0\'cc
\f0  
\f1 \'b5\'e9\'be\'ee\'b0\'a1\'b4\'c2
\f0  
\f1 \'b0\'c5\'b4\'cf\'b1\'ee
\f0 !\
class Solution \{\
    \
    void dfs(int[][] computers, int i, boolean[] visited) \{\
        visited[i] = true;\
        \
        for(int j=0; j<computers[i].length; j++) \{\
            if(i != j && computers[i][j] == 1 && visited[j] == false) \{\
                dfs(computers, j, visited);\
            \}\
        \}\
        \
    \}\
    \
    public int solution(int n, int[][] computers) \{\
        boolean[] visited = new boolean[n];\
        int answer = 0;\
        \
        for(int i=0; i<n; i++) \{\
            if(visited[i] == false) \{\
                dfs(computers, i, visited);\
                answer++;\
            \}\
        \}\
    \
        return answer;\
    \}\
\}}