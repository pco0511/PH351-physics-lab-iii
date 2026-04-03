# 물리학 실험 III 학생 매뉴얼

## S3. 제만 효과 (Zeeman Effect)

**KAIST 물리학과**

---

## 목차

1. [서론](#1-서론)
2. [이론](#2-이론)
   - 2.1 [전자 에너지 스펙트럼](#21-전자-에너지-스펙트럼)
   - 2.2 [제만 효과](#22-제만-효과)
3. 실험 과정
4. 데이터 해석 방법
5. 보고서 작성 지침

---

> **⚠ 주의!**
>
> **고온, 고전압**

---

## 1 서론

고전 양자역학에서, 원자는 원자핵과 전자 사이의 정전기적 퍼텐셜로부터 발생하는 이산적인(discrete) 에너지 스펙트럼으로 특징지어진다.

이러한 특성은 크게 두 가지 관측 방법으로 포착할 수 있다:

- 들뜬(excited) 전자가 높은 에너지 상태 $n$에서 낮은 에너지 상태 $m$ ($n > m$)으로 전이하면서 에너지 $E(n) - E(m)$을 가진 광자를 방출한다. (예: Ly$\alpha$, 형광(fluorescence))
- 낮은 에너지 상태 $n$에 있는 전자가 충분한 에너지를 가진 광자를 흡수하여 높은 에너지 상태 $m$ ($n < m$)으로 전이할 수 있다. (예: 외계행성 대기 분석)

위 예시들의 공통적인 핵심 특징은 방출되거나 흡수되는 빛(광자)이 단색광(monochromatic)이라는 것이다. 다시 말해, 각 전이 $n \leftrightarrow m$에 대해 하나의 파장만이 선택된다. 이는 전자의 에너지가 주양자수(principal quantum number) $n$에만 의존하고, 궤도 양자수(orbital quantum number) $l$과 자기 양자수(magnetic quantum number) $m$에 대해서는 축퇴(degenerate)되어 있기 때문이다. 이러한 축퇴는 외부 전기장이나 자기장을 인가함으로써 해소할 수 있다. 두 경우 모두 하나의 주양자수에 대응하는 방출선 또는 흡수선의 분리를 초래한다. 전자의 경우를 슈타르크 효과(Stark effect)라 하고, 후자의 경우를 제만 효과(Zeeman effect)라 한다.

본 실험에서는 보어 마그네톤(Bohr magneton) $\mu_B$를 계산함으로써 제만 효과를 관측하고 검증한다.

---

## 2 이론

### 2.1 전자 에너지 스펙트럼

원자는 원자핵과 전자로 구성된다. 원자핵과 전자 사이의 정전기적 상호작용은 전자의 허용 에너지를 이산적으로 만들며, 이를 스펙트럼이라 한다.

전자는 두 에너지 준위 사이의 에너지 차이를 빛(광자)의 형태로 흡수하거나 방출함으로써 허용된 에너지 사이를 이동할 수 있다. 흡수 또는 방출되는 빛의 파장을 $\lambda$라 하면, $\lambda$에 대해 다음 공식이 성립한다:

$$\frac{1}{\lambda} = A \left| E_1 - E_2 \right| \tag{1}$$

여기서 $A$는 수치 상수이다. 해밀토니안이 다음과 같이 주어지는 수소 원자의 경우(하위 보정(sub-leading correction)을 무시),

$$H_{\text{hy}} = \frac{p^2}{2m_e} - \frac{1}{4\pi\epsilon_0} \frac{e^2}{r} \tag{2}$$

식 (1)은 다음과 같이 다시 쓸 수 있다:

$$\frac{1}{\lambda} = A \left| E_1 - E_2 \right| = R_H \left| \frac{1}{n^2} - \frac{1}{m^2} \right| \tag{3}$$

여기서 $n$, $m$은 두 에너지 준위에 대응하는 주양자수이고, $R_H$는 뤼드베리 상수(Rydberg's constant)라 불린다. 파장이 궤도 양자수나 자기 양자수가 아닌 주양자수에만 의존함에 주목하라.

### 2.2 제만 효과

단일 전자는 두 종류의 각운동량을 가진다:

- **궤도 각운동량(Orbital angular momentum)** $\mathbf{L}$: 양성자에 대한 상대적 궤도 운동에 기인한다.
- **스핀 각운동량(Spin angular momentum)** $\mathbf{S}$: 스핀이라 불리는 입자의 고유한(intrinsic) 물리량에 기인한다.

이 두 물리량은 단일 전자에 대한 자기 쌍극자 모멘트(magnetic dipole moment)를 형성한다:

$$\boldsymbol{\mu}_l = -\frac{e}{2m}\mathbf{L}, \qquad \boldsymbol{\mu}_s = -\frac{e}{m}\mathbf{S} \tag{4}$$

균일한 외부 자기장 $\mathbf{B}$가 있을 때, 계는 $\delta H$에 의해 섭동을 받는다:

$$\delta H = -\boldsymbol{\mu} \cdot \mathbf{B} = \frac{e}{2m}(\mathbf{L} + 2\mathbf{S}) \cdot \mathbf{B} \tag{5}$$

섭동 계산을 이용하면, 이제 전자의 에너지 준위는 주양자수뿐만 아니라 자기 양자수에도 의존하게 된다. 제만 보정(Zeeman correction)이라 불리는 에너지 이동은 다음과 같이 주어진다:

$$\Delta E = \mu_B g_J B_{\text{ext}} \Delta m \tag{6}$$

여기서 $\mu_B$는 보어 마그네톤(Bohr magneton), $g_J$는 란데 g-인자(Landé g-factor), $m$은 관심 대상인 자기 양자수이다.

<!-- Figure 1: 카드뮴 방출선에서 관측되는 정상 제만 효과. 원칙적으로 5 × 3 = 15개의 전이가 허용되지만, 선택 규칙(selection rule)에 의해 실제로는 9개만 허용된다. -->

![[Pasted image 20260403084328.png]]

**그림 1.** 카드뮴(Cadmium) 방출선에서 관측되는 정상 제만 효과. 원칙적으로 $5 \times 3 = 15$개의 전이가 허용되지만, 선택 규칙(selection rule)에 의해 실제로는 9개만 허용된다.

<!-- Figure 2: 궤도 구조에 의한 방출선의 편광. 우리는 횡편광(transverse polarization)을 관측할 것이다. 물론, 종편광(longitudinal polarization)은 존재하지 않는다(그리고 절대 존재하지 않는다). -->

![[Pasted image 20260403084345.png]]

**그림 2.** 궤도 구조에 의한 방출선의 편광. 우리는 횡편광(transverse polarization)을 관측할 것이다. 물론, 종편광(longitudinal polarization)은 존재하지 않는다(그리고 절대 존재하지 않는다).

---

## 3 실험 과정

본 실험의 목적은 정상 제만 효과(normal Zeeman effect)를 관측하고, 데이터로부터 보어 마그네톤을 계산하는 것이다. 실험 과정은 다음과 같다.

1. 카드뮴(Cd) 램프를 켜고, 밝은 청색 빛을 방출하기 시작할 때까지 기다린다.

2. 컴퓨터에 준비된 카메라 소프트웨어를 실행한다. 주로 빨간색, 초록색, 파란색으로 구성된 다양한 색상의 원형 고리(annulus) 패턴을 볼 수 있는지 확인한다. 또한 편광판(polarizer)을 회전시키면서 방출광의 $\sigma$-편광과 $\pi$-편광을 구분해 본다. 그림 2를 참고하라.

3. 가우스 미터(gauss meter)를 사용하여 자기장의 크기를 측정한다.

4. 파브리-페로 간섭계(Fabry-Perot interferometer)에 빨간색 필터를 삽입한다. 이제 빨간색 고리만 보이게 된다. 고리의 반지름 $r_i^a$를 측정한다. 아래 첨자 $i$는 $i$번째 간섭 차수(order of interference)의 반지름을 측정한다는 의미이다. 제만 효과에 의해 고리가 두 개의 인접한 고리로 분리될 수 있다. 이때 $r_i^a$는 *$i$번째 간섭 차수의 $a$번째 인접 고리*의 반지름을 측정한다는 의미이다. 인접한 두 선을 볼 수 없다면, 각 간섭 차수에 대해 단일 고리의 반지름만 측정하면 된다. 최종적으로 $r_1^1, r_1^2;\; r_2^1, r_2^2;\; r_3^1, r_3^2;\; r_4^1, r_4^2;\; \cdots$ 와 같은 형태의 데이터를 얻어야 한다[^1]. 각 자기장과 편광에 대해 동일한 작업을 수행한다.

5. 빨간색 필터를 제거하고 초록색 필터를 삽입한다. 이제 초록색(또는 청색처럼 보이는) 고리만 보이게 된다. 3번에서 설명한 것과 동일한 작업을 수행한다.

6. 자석에 부착된 나사를 풀거나 조여서 자석 사이의 거리(즉, 자기장의 크기)를 조절한다. **나사를 너무 많이 풀거나 조이지 마라.** 실험 장치 전체가 망가질 수 있다. 이제 과정 3으로 돌아가서 위의 동일한 작업을 반복한다.

[^1]: 최소 4차(order)까지 측정하라.

<!-- Figure 3: 실험 장치 구성도 -->

![[Pasted image 20260403084601.png]]

**그림 3.** 실험 장치 구성도.

| 번호 | 이름 |
|:---:|:---|
| 1 | 카드뮴 램프 |
| 2 | 거리 조절이 가능한 한 쌍의 자석 |
| 3 | L₁ ($f = 50$ mm) |
| 4 | 파브리-페로 간섭계, 폭 = 3 mm |
| 5 | L₂ ($f = 300$ mm) |
| 6 | 편광판(Polarizer) |
| 7 | L₃ ($f = 50$ mm) |
| 8 | 카메라 |
| 9 | 가우스 미터 |
| 10 | 색필터 (빨간색, 초록색) |
| 11* | 개인 USB 드라이브 (강력 권장) |

**표 1.** 구성 요소 목록.

---

## 4 데이터 해석 방법

파브리-페로 간섭계는 제만 분리(Zeeman splitting)를 파장의 수(number of wavelengths)로 정량적으로 측정하는 데 사용된다.

간섭계(이하 intf.)는 내부 표면에 부분 투과 금속층이 코팅된 두 장의 평행한 평판 유리로 구성된다. 그림 4에서 거리 $t = 3$ mm로 떨어진 두 부분 투과면 (1)과 (2)를 생각하자. 판에 대한 법선과 각도 $\theta$를 이루며 입사하는 광선은 AB, CD, EF 등의 광선으로 분리된다. 두 인접한 광선(예를 들어 AB와 CD)의 파면(wave front) 사이의 경로차(path difference)는 $\delta = BC + CK$이며, 여기서 BK는 CD에 수직이고,

$$CK = BC \cos 2\theta \quad \text{그리고} \quad BC \cos \theta = t \tag{7}$$

이며 $t = 3$ mm이다. 따라서 $\delta = 2t\cos\theta$를 얻고, $n\lambda = 2t\cos\theta$ ($n \in \mathbb{Z}$)일 때 보강 간섭(constructive interference)이 일어난다. 판 사이 매질의 굴절률이 $\mu \neq 1$이면, 이 식은 다음과 같이 수정되어야 한다:

$$n\lambda = 2\mu t \cos\theta \tag{8}$$

<!-- Figure 4: 간섭계와 렌즈의 역할 -->

![[Pasted image 20260403085509.png]]

**그림 4.** 간섭계와 렌즈의 역할.

식 (8)은 기본 간섭계 방정식이다. 그림 4의 왼쪽에 보이는 것처럼, 평행 광선 B, D, F 등을 초점거리 $f$인 렌즈로 초점에 모으자. 그러면 $\theta$가 식 (8)을 만족할 때 스크린에 밝은 고리가 나타나며, 그 반지름은 다음과 같다:

$$r_n = f\tan\theta_n \simeq f\theta_n \tag{9}$$

여기서 $\theta_n$이 작은 값일 때 성립한다. 다음과 같이 정의하면,

$$n = \frac{2\mu t}{\lambda}\cos\theta_n \equiv n_0\cos\theta_n = n_0\left(1 - 2\sin^2\frac{\theta_n}{2}\right) \tag{10}$$

여기서 $n_0 \equiv \frac{2\mu t}{\lambda}$이다. 최종적으로 다음을 얻는다:

$$n \simeq n_0\left(1 - \frac{\theta_n^2}{2}\right) \quad \text{또는} \quad \theta_n \simeq \sqrt{\frac{2(n_0 - n)}{n_0}} \tag{11}$$

$\theta_n$이 밝은 무늬(bright fringe)에 대응하면 $n$은 정수여야 한다. 그러나 중심에서의 간섭을 나타내는 $n_0$는 일반적으로 정수가 아니다. $n_1$이 첫 번째 고리의 간섭 차수라 하면, $n_1 = n_0\cos\theta_{n_1}$이므로 분명히 $n_1 < n_0$이다. 그러면 다음과 같이 놓자:

$$n_1 = n_0 - \epsilon \quad (0 < \epsilon < 1) \tag{12}$$

여기서 $n_1$은 $n_0$에 가장 가까운 정수이다. 따라서 중심으로부터 바깥쪽으로 세어 $p$번째 고리에 대해 일반적으로 다음이 성립한다:

$$n_p = (n_0 - \epsilon) - (p - 1) \tag{13}$$

식 (13)을 식 (9), (11)과 결합하면, $r_{n_p}$를 $r_p$로 대체하여 고리의 반지름을 얻는다:

$$r_p = \sqrt{\frac{2f^2}{n_0}} \cdot \sqrt{(p-1) + \epsilon} \tag{14}$$

인접한 고리의 반지름 제곱의 차이가 상수임에 주목하라:

$$r_{p+1}^2 - r_p^2 = \frac{2f^2}{n_0} \tag{15}$$

$\epsilon$은 $r_p^2$를 $p$에 대해 그래프로 그리
e고 $r_p^2 = 0$으로 외삽(extrapolation)함으로써 그래프적으로 결정할 수 있다.

이제, 서로 매우 가까운 파장 $\lambda_a$와 $\lambda_b$를 가진 두 스펙트럼선 성분(하나의 중심선이 두 성분으로 분리)이 있다면, 중심에서의 분수 차수(fractional order)는 $\epsilon_a$와 $\epsilon_b$이다:

$$\epsilon_a = \frac{2\mu t}{\lambda_a} - n_{1,a} \equiv 2\mu t \bar{\nu}_a - n_{1,a}$$

$$\epsilon_b = \frac{2\mu t}{\lambda_b} - n_{1,b} \equiv 2\mu t \bar{\nu}_b - n_{1,b} \tag{16}$$

여기서 $n_{1,a}$와 $n_{1,b}$는 첫 번째 고리의 간섭 차수이다. 따라서, 고리가 전체 차수만큼 겹치지 않으면 $n_{1,a} = n_{1,b}$이고, 두 성분 사이의 파수(wavenumber) 차이는 단순히 다음과 같다:

$$\Delta\bar{\nu} = \bar{\nu}_a - \bar{\nu}_b = \frac{\epsilon_a - \epsilon_b}{2\mu t} \tag{17}$$

또한, 식 (14)와 (15)를 이용하면 다음을 얻는다:

$$\frac{(r_{p+1}^a)^2}{(r_{p+1})^2 - (r_p)^2} - p = \epsilon \tag{18}$$

이 항등식은 성분별로 적용할 수 있다. 즉,

$$\frac{(r_{p+1}^a)^2}{(r_{p+1}^a)^2 - (r_p^a)^2} - p = \epsilon_a$$

$$\frac{(r_{p+1}^b)^2}{(r_{p+1}^b)^2 - (r_p^b)^2} - p = \epsilon_b \tag{19}$$

이 분수 차수들을 식 (17)에 대입하면, 파수 차이에 대해 다음을 얻는다:

$$\Delta\bar{\nu} = \frac{1}{2\mu t}\left[\frac{(r_{p+1}^a)^2}{(r_{p+1}^a)^2 - (r_p^a)^2} - \frac{(r_{p+1}^b)^2}{(r_{p+1}^b)^2 - (r_p^b)^2}\right] \tag{20}$$

식 (15)에서 성분 $a$의 반지름 제곱의 차이,

$$\Delta_{p+1,p}^a = (r_{p+1}^a)^2 - (r_p^a)^2 = \frac{2f^2}{n_{0,a}} \tag{21}$$

는 성분 $b$의 동일한 차이와 (매우 작은 부분 이내에서) 같다:

$$\Delta_{p+1,p}^b = (r_{p+1}^b)^2 - (r_p^b)^2 = \frac{2f^2}{n_{0,b}} \tag{22}$$

따라서, $p$의 값에 관계없이 $\Delta_{p+1,p}^a = \Delta_{p+1,p}^b$이다. 마찬가지로, 모든 값

$$\delta_p^{a,b} = (r_p^a)^2 - (r_p^b)^2 \tag{23}$$

은 $p$에 관계없이 같으며, 서로 다른 $\Delta$ 값들에 대해서와 마찬가지로 평균을 취할 수 있다. $\delta$와 $\Delta$를 평균값으로 놓으면, $\mu = 1$을 예상하여, 성분 $a$와 $b$의 파수 차이는 다음과 같다:

$$\Delta\bar{\nu} = \frac{1}{2t}\frac{\delta}{\Delta} \tag{24}$$

각 자기장과 색필터 세트에 대해, 표 2와 같은 형태의 정사각 배열을 구성할 수 있다.

| 성분 | $p = 1$ | $p = 2$ | $p = 3$ | $p = 4$ |
|:---:|:---:|:---:|:---:|:---:|
| $a$ | $r_1^a$ | $r_2^a$ | $r_3^a$ | $r_4^a$ |
| $b$ | $r_1^b$ | $r_2^b$ | $r_3^b$ | $r_4^b$ |

**표 2.** 하나의 자기장과 삽입된 색필터에 대한 데이터 예시.

평균값 $\Delta$와 $\delta$는 다음과 같이 계산한다[^2]:

$$\Delta = \frac{1}{4}\sum_{p=1}^{2}\left(\Delta_{2p+1,2p}^a + \Delta_{2p+1,2p}^b\right)$$

$$\delta = \frac{1}{4}\sum_{p=1}^{4}\delta_p^{a,b} \tag{25}$$

[^2]: 사용 가능한 모든 $\Delta$를 사용할 수 있는 것은 아니다. 교대로(alternate) 사용해야 정보 손실을 피할 수 있다.

분리된 선 중 하나와 중심선 사이의 파수 차이는 $\Delta\bar{\nu}/2$이다. 복사하는 전자에게 이것은 다음의 에너지 변화를 의미한다:

$$\Delta E = \frac{hc\Delta\bar{\nu}}{2} \tag{26}$$

한편, 에너지 변화 $\Delta E$는 자기 플럭스 밀도(magnetic flux density) $B$에 비례한다. $\Delta E$와 $B$ 사이의 비례 상수가 보어 마그네톤 $\mu_B$이다[^3]:

$$\Delta E = \mu_B B \tag{27}$$

이 방정식들을 결합하면 $\mu_B$에 대한 식을 얻는다:

$$\mu_B = \frac{hc\Delta\bar{\nu}/2}{B} \tag{28}$$

여기서 $c$와 $h$는 각각 광속과 플랑크 상수이다. 데이터로부터 보어 마그네톤을 추출하고, $\mu_B$의 문헌값과 비교하라:

$$\mu_B = 9.2740100657 \times 10^{-24} \;\text{J/T} \tag{29}$$

[^3]: 여기서 선택 규칙에 의해 $\Delta m = \pm 1$이고, 정상 제만 효과를 다루고 있으므로 $g_J = 1$이다.

---

## 5 보고서 작성 지침

확인할 수 있듯이, 이 실험은 꽤 정확하다. 그림 5에 보이는 단 5개의 데이터점만으로도 선형 피팅(linear fitting)을 하면 99% 이상의 정확도를 얻을 수 있다. 권장하는 것은, 이 실험에서 포착할 수 있는 제만 효과의 이론적 측면에 대해 논의하는 것이다.

<!-- Figure 5: 예시 결과 그래프 -->

![[Pasted image 20260403085537.png]]

**그림 5.** 예시 결과 그래프.

---

## 참고문헌

[1] D.J. Griffiths and D.F. Schroeter, *Introduction to Quantum Mechanics*, Cambridge University Press, 3rd ed. (2018).

[2] PHYWE Laboratory experiment manual, *LEP 5.1.10 Zeeman Effect*.

[3] PARTICLE DATA GROUP collaboration, *Review of particle physics*, Phys. Rev. D **110** (2024) 030001.

[4] P.J. Mohr, D.B. Newell, B.N. Taylor and E. Tiesinga, *Codata recommended values of the fundamental physical constants: 2022*, Rev. Mod. Phys. **97** (2025) 025002.
