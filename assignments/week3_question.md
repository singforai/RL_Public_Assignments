# Week 3 Quiz
문제를 읽고, 괄호 안에 참/거짓 여부(O/X)를 표시하세요.
## Q. 1
강화학습은 비지도학습의 일종이다.

Reinforcement learning is a type of unsupervised learning.  (&nbsp;&nbsp;&nbsp;)
## Q. 2
강화학습은 전통적인 기계학습이 아닌, 제어 이론과 컴퓨터과학, 심리학, 신경과학에서 유래되었다.

Reinforcement learning comes from control theory, computer science, psychology, and neuroscience, not traditional machine learning. (&nbsp;&nbsp;&nbsp;)
## Q. 3
모든 환경에서, 이득 $G_t=\sum_{t=0}^\infty\gamma^iR_{t+i+1}$는 $\gamma=1$을 가질 수 있다.

In all environments, return $G_t=\sum_{t=0}^\infty\gamma^iR_{t+i+1}$ can satisfy $\gamma=1$. (&nbsp;&nbsp;&nbsp;)
## Q. 4
에이전트는 언제나 환경의 상태 $S_t^e$에 접근 가능하다.

The agent always has access to the state $S_t^e$ of the environment. (&nbsp;&nbsp;&nbsp;)
## Q. 5
상태 $S_t$가 information state이면, $S_{t+1}$과 $S_{t-1}$은 독립이다.

If state $S_t$ is an information state, then $S_{t+1}$ and $S_{t-1}$ are independent. (&nbsp;&nbsp;&nbsp;)
## Q. 6
상태 $S_t$가 information state이면, $S_{t}$ 가 주어졌을 때 $S_{t+1}$과 $S_{t-1}$은 조건부 독립이다.

If state $S_t$ is an information state, then $S_{t+1}$ and $S_{t-1}$ are conditionally independent given $S_{t}$. (&nbsp;&nbsp;&nbsp;)
## Q. 7
POMDP에서, $S_t^a = S_t^e$ 이다.

In a POMDP, $S_t^a = S_t^e$. (&nbsp;&nbsp;&nbsp;)
## Q. 8
MDP에서, $G_t$는 $t$ 시점에서 행동을 하는 즉시 얻을 수 있다.

In MDP, $G_t$ can be obtained as soon as an action is taken at time $t$. (&nbsp;&nbsp;&nbsp;)
## Q. 9
MRP에는 iterative method를 적용할 수 없다.

The iterative method cannot be applied to MRP. (&nbsp;&nbsp;&nbsp;)
## Q. 10
MDP의 정책은 시간에 영향을 받지 않는다.

MDP's policies are time-independent. (&nbsp;&nbsp;&nbsp;)
## Q. 11
모든 MDP에는 단 하나의 최적 가치 함수가 존재한다.

For every MDP, there is only one optimal value function. (&nbsp;&nbsp;&nbsp;)
## Q. 12
모든 MDP에는 단 하나의 최적 정책이 존재한다.

For every MDP, there is only one optimal policy. (&nbsp;&nbsp;&nbsp;)
## Q. 13
모든 MDP에는 optimal value function의 closed form solution이 존재한다.

For every MDP, there exists a closed form solution of the optimal value function. (&nbsp;&nbsp;&nbsp;)

# Challanges
아래 문제는 관심 있는 사람을 위한 심화 문제입니다. 풀지 않아도 불이익은 없습니다.

The questions below are advanced questions for those who are interested. There is no penalty for not solving them.
## Challange 1
Quiz 6의 답을 Information state의 정의
$$\mathbb{P}[S_{t+1}|S_t]=\mathbb{P}[S_{t+1}|S_1,\ldots,S_t]$$
를 이용하여 보이시오. (힌트: 전확률의 공식을 사용하시오.)

Prove your answer to Quiz 6 using the definition of an information state
$$\mathbb{P}[S_{t+1}|S_t]=\mathbb{P}[S_{t+1}|S_1,\ldots,S_t].$$
(Hint: Use the total probability formula).
## Challange 2
$$\mathbb{E}\left[f(X)\right]
=\lim_{n\to\infty}\frac1n\sum_{i=1}^nf(X^{(i)})
\approx\frac1m\sum_{i=1}^mf(X^{(i)})$$
위 식은 수리통계에서의 추정량의 평균과, 실제 $m$개의 샘플을 이용하여 그것을 구하는 근사 방법을 제공한다. 단순히 말하자면, 모분포에서 $m$개의 표본을 뽑은 뒤 평균을 내는 것이다.

이제 우리에게 어떤 환경 시뮬레이터와 정책 $\pi$, 시작 상태 $s_0$가 주어졌다고 했을 때, $v_\pi(s_0)=\mathbb{E}[G_0|S_0=s_0]$를 추정하기 위한 가장 단순한 방법은 무엇인가?

The above expression provides the mean of an estimate in mathematical statistics and an approximate way to find it using $m$ actual samples. Simply put, we draw $m$ samples from the parent distribution and average them.

Now, given an environment simulator, a policy $\pi$, and a starting state $s_0$, what is the simplest way to estimate $v_\pi(s_0)=\mathbb{E}[G_0|S_0=s_0]$?
## Challange 3
Bellman Equation의 유도 중 핵심적인 부분은 다음과 같다.
$$v(s)=\mathbb{E}\left[R_{t+1}+\gamma G_{t+1}\middle|S_t=s\right]\\
=\mathbb{E}\left[R_{t+1}+\gamma v(S_{t+1})\middle|S_t=s\right]$$
첫째 줄의 $G_{t+1}$은 왜 두번째 줄의 $v(S_{t+1})$으로 변하는가? 수리통계적으로 위 식이 성립함을 보이시오.

The key part of the derivation of the Bellman Equation is as follows:
$$v(s)=\mathbb{E}\left[R_{t+1}+\gamma G_{t+1}\middle|S_t=s\right]\\
=\mathbb{E}\left[R_{t+1}+\gamma v(S_{t+1})\middle|S_t=s\right].$$
Why does $G_{t+1}$ in the first line change to $v(S_{t+1})$ in the second line? Show that the above expression holds mathematically.
