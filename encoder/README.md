
export PYTHONPATH=/opt/ibm/ILOG/CPLEX_Studio_Community1210/cplex/python/3.7/x86-64_linux/



# How to use

This document describes how to run the team formation translator.
The available **mode** are:
* tf, classical team formation
* ktf,
* ptf,
* ftf,


## Notation

Here is a bunch of notation that will be use in the rest of this note.
We use upper-case letters to describe objects that are about the high level problem.
The team formation problem consider a set of agents $\mathcal{A}$ and and set of skills $\mathcal{S}$.
$A_i$ is the notation used in order to reference the agent i, and $S_j$ references the
skill $j$. We simply note $S(A_i)$ the set of skills of the agent $A_i$ and $A(S_j)$ the
set of agents that support the skill $S_j$.
For each agent we also assign two kind of deployment cost regarding if the agent $A_i$
is deployed in first $w_1(A_i)$ or second $w_2(A_i)$ round. Each skill receives also a weight
regarding its importance in the process, this weight is noted $w_s(S_j)$.
Agents that cannot be deployed at the phase $f$ receive a weight of $-1$. Some pair $(A_i, A_j)$
of agents cannot be associate, in this case we say that they are in exclusion, noted $A_i \oplus A_j$.

**Example**: Here is a complete example we will use in the rest of the document. It contains 14 agents
$\{A_0, A_1, \ldots, A_{13}\}$ and 5 skills $\{S_0, S_1, S_2, S_3, S_4\}$. We have:

* For each agent the skills it supports:
  - $S(A_0)$ = $\{S_0\}$
  - $S(A_1)$ = $\{S_0, S_1, S_2\}$
  - $S(A_2)$ = $\{S_1\}$
  - $S(A_3)$ = $\{S_0, S_1, S_3\}$
  - $S(A_4)$ = $\{S_2\}$
  - $S(A_5)$ = $\{S_0, S_2, S_3\}$
  - $S(A_6)$ = $\{S_3\}$
  - $S(A_7)$ = $\{S_1, S_2, S_3, S_4\}$
  - $S(A_8)$ = $\{S_4\}$
  - $S(A_9)$ = $\{S_3, S_4\}$
  - $S(A_{10})$ = $\{S_4\}$
  - $S(A_{11})$ = $\{S_2\}$
  - $S(A_{12})$ = $\{S_3\}$
  - $S(A_{13})$ = $\{S_4\}$


* For each skill the list of agents that endorse it:
  - $A(S_0)$ = $\{A_0, A_1, A_3, A_5\}$
  - $A(S_1)$ = $\{A_1, A_2, A_3\}$
  - $A(S_2)$ = $\{A_1, A_4, A_5, A_7, A_{11}\}$
  - $A(S_3)$ = $\{A_3, A_5, A_7, A_9, A_{12}\}$
  - $A(S_4)$ = $\{A_7, A_8, A_9, A_{10}, A_{13}\}$

* The weights for the different phases are:
  - $w_1(A_0) = 100$ and $w_2(A_0) = 300$
  - $w_1(A_1) = 200$ and $w_2(A_1) = -1$
  - $w_1(A_2) = 100$ and $w_2(A_2) = 300$
  - $w_1(A_3) = 200$ and $w_2(A_3) = -1$
  - $w_1(A_4) = 100$ and $w_2(A_4) = 300$
  - $w_1(A_5) = 200$ and $w_2(A_5) = -1$
  - $w_1(A_6) = 100$ and $w_2(A_6) = 300$
  - $w_1(A_7) = 200$ and $w_2(A_7) = -1$
  - $w_1(A_8) = 100$ and $w_2(A_8) = 300$
  - $w_1(A_9) = 200$ and $w_2(A_9) = -1$
  - $w_1(A_{10}) = 200$ and $w_2(A_{10}) = -1$
  - $w_1(A_{11}) = 200$ and $w_2(A_{11}) = -1$
  - $w_1(A_{12}) = 200$ and $w_2(A_{12}) = -1$
  - $w_1(A_{13}) = 200$ and $w_2(A_{13}) = -1$

* The weight for the difference skills:
  - $w_s(S_0) = 4$
  - $w_s(S_0) = 6$
  - $w_s(S_0) = 1$
  - $w_s(S_0) = 4$
  - $w_s(S_0) = 2$

* Finally we have a bunch of exclusion constraints:
  - $A_0 \oplus A_1$
  - $A_2 \oplus A_3$
  - $A_4 \oplus A_5$
  - $A_6 \oplus A_7$
  - $A_8 \oplus A_9$

We use the classical propositional logic, and more precisely SAT.
Lower-case letters to describe propositional variables. In the following $a_i$ references
the agent $A_i$ and $s_j$ references the skill $S_j$.


## Format

Here the input file that describes the running example presented in the previous section.

```
p 14 5
a 0 100 300 0
a 1 200 -1 0 1 2
a 2 100 300 1
a 3 200 -1 0 1 3
a 4 100 300 2
a 5 200 -1 0 2 3
a 6 100 300 3
a 7 200 -1 1 2 3 4
a 8 100 300 4
a 9 200 -1 3 4
a 10 200 -1 4
a 11 200 -1 2
a 12 200 -1 3
a 13 200 -1 4
s 0 4
s 1 6
s 2 1
s 3 4
s 4 2
e 0 1
e 2 3
e 4 5
e 6 7
e 8 9
```



## Team Formation (TF)

Firstly, let us encode the problem that consists in finding a team such that all the skills
are covered and exclusion constraints are satisfied.
To be sure that all the skills are covered it is enough that at least one agent
that endorse each skill individually. If we consider our running example,
to accomplish the skill $S_0$ it is necessary that at least one agent of $\{A_0, A_1, A_3, A_5\}$
is present. Then, the propositional logic encoding is simply:
\[
\bigwedge_{S_j \in \mathcal{S}} ~~~ \bigvee_{A_i \in A(S_j)} a_i
\]
That gives for our running example the following clauses:
\[
(a_0 \vee a_1 \vee a_3 \vee a_5) \wedge
(a_1 \vee a_2 \vee a_3) \wedge
(a_1 \vee a_4 \vee a_5 \vee a_7 \vee a_{11}) \wedge \\
(a_3 \vee a_5 \vee a_7 \vee a_9 \vee a_{12}) \wedge
(a_7 \vee a_8 \vee a_9 \vee a_{10} \vee a_{13})
\]

Because some combination $A_i \oplus A_j$ of agents are impossible we also need
to express exclusion constraints. To do so, it is enough to add binary such that $\neg a_i \vee \neg a_j$.
That gives for our running example the following clauses:
\[
(\neg a_0 \vee \neg a_1) \wedge (\neg a_2 \vee \neg a_3) \wedge (\neg a_4 \vee \neg a_5)
 \wedge (\neg a_6 \vee \neg a_7) \wedge (\neg a_8 \vee \neg a_9)
\]

The objective is then to find out a team $\mathcal{T} \subseteq \mathcal{A}$
that minimizes the deployment cost $\sum_{A_i \in T} w_1(A_i)$. Such kind of constraints
is not handle in classical SAT, we need to consider weighted partial MaxSAT problem
that consists in finding an assignment that satisfies a set of clauses, called hard clauses,
while maximizing the weight $c_i$ of the clauses $\alpha_i$ that are not satisfied in
the soft clause $(\alpha_i, c_i)$. For our running example we will add the following set of
soft clauses:
\[
\{(\neg a_0, 100),(\neg a_1, 200),(\neg a_2, 100),(\neg a_3, 200),(\neg a_4, 100),(\neg a_5, 200),\\
(\neg a_6, 100),(\neg a_7, 200),(\neg a_8, 100),(\neg a_9, 200),(\neg a_{10}, 200), (\neg a_{11}, 200),\\
   (\neg a_{12}, 200),(\neg a_{13}, 200)\}
\]

That gives, following the DIMACS format, the following input file:
```
p wcnf 14 24 2301
c hard part
2301 1 2 4 6 0
2301 2 3 4 8 0
2301 2 5 6 8 12 0
2301 4 6 7 8 10 13 0
2301 8 9 10 11 14 0
2301 -1 -2 0
2301 -3 -4 0
2301 -5 -6 0
2301 -7 -8 0
2301 -9 -10 0
c soft part
100 -1 0
200 -2 0
100 -3 0
200 -4 0
100 -5 0
200 -6 0
100 -7 0
200 -8 0
100 -9 0
200 -10 0
200 -11 0
200 -12 0
200 -13 0
200 -14 0
```

Here is the command line needed to generate this file using our application:
```python
python3 ./translator.py BENCH.txt -tf
```

It is also possible to directly solve the problem by specifying the MaxSAT solver path
(**../LMHS/bin/LMHS** for example).
```python
python3 ./translator.py BENCH.txt -tf -solve=SolverPath
```
