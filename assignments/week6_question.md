# Week 6 Quiz
문제를 읽고, 괄호 안에 참/거짓 여부(O/X)를 표시하세요.
## Q. 1
DP가 적용되는 문제는 재귀적인 최적 부분구조와 재사용 가능한 부분 해를 가진다.

Problems to which DP is applied have a recursive optimal substructure and reusable partial solutions. 
(&nbsp;&nbsp;&nbsp;)

## Q. 2
MDP에는 DP를 적용할 수 있다.

DP can be applied to MDPs. (&nbsp;&nbsp;&nbsp;)

## Q. 3
DP를 이용한 반복 정책 평가는 실제 가치함수 $v_\pi$ 로 수렴한다.

Iterative policy evaluation using DP converges to the true value function $v_\pi$. (&nbsp;&nbsp;&nbsp;)

## Q. 4
정책 반복은 정책 평가와 정책 향상 단계의 순차적 반복이다.

A policy iteration is a sequential iteration of the policy evaluation and policy improvement phases. (&nbsp;&nbsp;&nbsp;)

## Q. 5
DP 강의 자료 16페이지 (혹은 Sutton, 2020 의 그림 4.2)의 Jack's Car Rental 예제에서, 시작 정책은 푸아송 분포을 따르지 않는다.

In the Jack's Car Rental example on page 16 of the DP lecture notes (or Figure 4.2 in Sutton, 2020), the startup policy does not follow a Poisson distribution. (&nbsp;&nbsp;&nbsp;)

## Q. 6
정책 반복을 이용해 최적 정책을 구할 수 있다.

You can use policy iteration to find the optimal policy. (&nbsp;&nbsp;&nbsp;)

## Q. 7
가치 반복은 초기 정책이 명시적으로 주어져야 한다.

Value iteration requires the initial policy to be explicitly given. (&nbsp;&nbsp;&nbsp;)

## Q. 8
Prioritized Sweeping은 Bellman error가 큰 상태를 우선하여 업데이트한다.
 
Prioritized Sweeping updates states with large Bellman errors first. (&nbsp;&nbsp;&nbsp;)

## Q. 9
**차원의 저주**라는 용어를 최초로 제안한 사람은 벨만이다. 

It was Bellman who first proposed the term **curse of dimensionality**. (&nbsp;&nbsp;&nbsp;)

## Q. 10
MDP의 차원 문제를 해결하기 위해 sample backup 방법을 쓸 수 있다. 

To solve the dimensionality problem in MDPs, you can use the sample backup method. (&nbsp;&nbsp;&nbsp;)

## Q. 11
MDP가 복잡하면 Model-free method를 쓸 수 없다. 
 
If your MDP is complex, you can't use a model-free method. (&nbsp;&nbsp;&nbsp;)

## Q. 12
MC 방법은 큰 수의 법칙으로 지지된다. 

The MC method is supported by the law of large numbers. (&nbsp;&nbsp;&nbsp;)

## Q. 13
Incremental mean은 이전 step의 평균과, step에 상관없이 고정된 상수값을 곱한 항을 포함한다. 

Incremental mean contains the average of the previous step, multiplied by a constant value that is fixed regardless of the step. (&nbsp;&nbsp;&nbsp;)

## Q. 14
TD는 bootstrapping을 이용하여 수렴 속도가 빠르지만, 이 때문에 bias가 생긴다. 

TD uses bootstrapping to converge faster, but this causes bias. (&nbsp;&nbsp;&nbsp;)

## Q. 15
MC는 episodic 환경에서만 사용할 수 있다. 

MC is only available in episodic environments. (&nbsp;&nbsp;&nbsp;)

## Q. 16
True TD Target $R_{t+1}+\gamma v_\pi\left(S_{t+1}\right)$의 조건부 기댓값 $\mathbb{E}\left[R_{t+1}+\gamma v_\pi\left(S_{t+1}\right)\middle|S_t\right]$은 가치함수 $v_\pi(S_t)$와 같다.
 
The conditional expectation $\mathbb{E}\left[R_{t+1}+\gamma v_\pi\left(S_{t+1}\right)\middle|S_t\right]$ of the True TD Target $R_{t+1}+\gamma v_\pi\left(S_{t+1}\right)$ is equal to the value function $v_\pi(S_t)$. (&nbsp;&nbsp;&nbsp;)

## Q. 17
TD Target $R_{t+1}+\gamma V_\pi\left(S_{t+1}\right)$의 조건부 기댓값 $\mathbb{E}\left[R_{t+1}+\gamma V_\pi\left(S_{t+1}\right)\middle|S_t\right]$은 가치함수 $v_\pi(S_t)$와 같다. 

The conditional expected value $\mathbb{E}\left[R_{t+1}+\gamma V_\pi\left(S_{t+1}\right)\middle|S_t\right]$ of TD Target $R_{t+1}+\gamma V_\pi\left(S_{t+1}\right)$ is equal to the value function $v_\pi(S_t)$. (&nbsp;&nbsp;&nbsp;)

## Q. 18
샘플들의 Maximum likelihood MDP는 MC 방법만으로 구할 수 있다. 

The maximum likelihood MDP of the samples can be obtained by the MC method alone. (&nbsp;&nbsp;&nbsp;)

## Q. 19
n-step return은 n이 커질수록 MC 방법의 return으로 수렴한다.
 
The n-step return converges to the return of the MC method as n gets larger. (&nbsp;&nbsp;&nbsp;)

## Q. 20
Episodic 환경의 $G_t^\lambda$는 $\left[(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}\right]+\lambda^{T-t-1}G_t$으로 정의할 수 있다. 

In the Episodic environment, $G_t^\lambda$ can be defined as $\left[(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}\right]+\lambda^{T-t-1}G_t$. (&nbsp;&nbsp;&nbsp;)

## Q. 21
Forward-View TD($\lambda$)로 on-line learning을 구현할 수 있다. 

Forward-View TD($\lambda$) can be used to implement on-line learning. (&nbsp;&nbsp;&nbsp;)

## Q. 22
TD(1)은 every-visit MC와 유사하다.

TD(1) is similar to every-visit MC. (&nbsp;&nbsp;&nbsp;)

## Q. 23
Importance sampling은 Markov 성질을 이용해 쪼갤 수 있다.

Importance sampling can be decomposed using Markov properties. (&nbsp;&nbsp;&nbsp;)

## Q. 24
Importance sampling은 두 분포간의 차이가 커도 안정하다.

Importance sampling is stable even when the difference between the two distributions is large. (&nbsp;&nbsp;&nbsp;)

## Q. 25
On-policy 방법은 다른 정책의 경험을 학습할 수 있다.

On-policy methods can learn from the experience of other policies. (&nbsp;&nbsp;&nbsp;)

## Q. 26
MDP의 환경 $p(s',r|s,a)$이 주어진다면 상태 가치 함수만으로 Greedy policy improvement가 가능하다.

Given the environment $p(s',r|s,a)$ of the MDP, it is possible to improve the greedy policy using only the state value function. (&nbsp;&nbsp;&nbsp;)

## Q. 27
$\epsilon$-Greedy 정책에서, $\pi(a|s)$가 가장 기대 이득이 높은 행동을 선택할 확률은 $\frac{m+(1-m)\epsilon}{m}$이다.

In an $\epsilon$-Greedy policy, the probability that $\pi(a|s)$ chooses the behavior with the highest expected return is $\frac{m+(1-m)\epsilon}{m}$. (&nbsp;&nbsp;&nbsp;)

## Q. 28
GLIE 조건은 MC 방법의 최적 행동 가치 함수로의 수렴을 보장한다. 

The GLIE condition guarantees the convergence of the MC method to the optimal action value function. (&nbsp;&nbsp;&nbsp;)

## Q. 29
GLIE 조건은 Sarsa의 최적 행동 가치 함수로의 수렴을 보장한다. 

The GLIE condition guarantees convergence to Sarsa's optimal action value function. (&nbsp;&nbsp;&nbsp;)

## Q. 30
Off-policy TD는 off-policy MC보다 Importance sampling ratio가 크다. 

Off-policy TDs have a larger Importance sampling ratio than off-policy MCs. (&nbsp;&nbsp;&nbsp;)

# Challanges
아래 문제는 관심 있는 사람을 위한 심화 문제입니다. 풀지 않아도 불이익은 없습니다.

The questions below are advanced questions for those who are interested. There is no penalty for not solving them.
## Challange 1
Contraction mapping theorem (or Banach fixed point theorem)는 policy evaluation과 policy iteration의 수렴을 보장한다.
그렇다면, 이 정리에서 Bellman optimality backup operator $T^*$은 실제 DP 알고리즘의 어떤 단계에 대응되는가?
또한 모든 벡터가 하나의 고정점으로 수렴한다는 것이 MDP에서 어떤 의미를 가지는가? 

The Contraction mapping theorem (or Banach fixed point theorem) guarantees the convergence of policy evaluation and policy iteration.
So, in this theorem, what step of the actual DP algorithm does the Bellman optimality backup operator $T^*$ correspond to?
Also, what does it mean for MDPs that all vectors converge to a single fixed point?

## Challange 2
Q-learning은 Off policy learning의 일종으로 볼 수 있다.
Q-learning이 epsilon greedy와 greedy 정책에 대한 importance sampling off-policy learning과 유사함을 
$$\mathbb{E}_{A_t\sim\mu(\cdot|S_t)}\left[\frac{\pi(A_t|S_t)}{\mu(A_t|S_t)}Q(S_t,A_t)\right]$$
위 식으로부터 유도하시오.

Q-learning can be viewed as a type of off-policy learning.
Show that Q-learning is similar to importance sampling off-policy learning for epsilon greedy and greedy policies by using the following equations: 
$$\mathbb{E}_{A_t\sim\mu(\cdot|S_t)}\left[\frac{\pi(A_t|S_t)}{\mu(A_t|S_t)}Q(S_t,A_t)\right].$$

