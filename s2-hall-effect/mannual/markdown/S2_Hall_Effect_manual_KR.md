i # p-Ge에서의 Hall Effect

## 1. 실험 목적

p-doped germanium에서 Hall effect를 관찰하고, 다음을 수행한다:

- 일정한 magnetic field에서 전류의 함수로 Hall voltage를 측정하여 **charge carrier의 density와 mobility**를 결정한다.
- 일정한 전류에서 magnetic field의 함수로 Hall voltage를 측정하여 **Hall coefficient**를 결정한다.

> **참고:** 온도에 따른 Hall voltage 측정 실험 및 Band gap 실험은 본 실험에서 생략한다.

---

## 2. 원리 (Principle)

### 2.1 Hall Effect 개요

Hall effect는 금속 또는 도핑된 반도체에서 charge transport의 미시적 매개변수를 결정하기 위한 중요한 실험적 방법이다.

본 실험에서는 p-doped germanium의 직사각형 시료를 균일한 magnetic field $B$ 안에 놓는다 (Fig. 1 참조). 시료에 전류 $I$가 흐르면, magnetic field $B$와 전류 $I$에 수직한 방향으로 전기적 전압(Hall voltage)이 발생한다:

$$U_H = R_H \cdot \frac{I \cdot B}{d} \tag{I}$$

여기서 $d$는 시료의 두께이고, $R_H$는 **Hall coefficient**로서 물질과 온도에 따라 달라진다.

![Fig. 1: 두께 d, 높이 b, 길이 w인 직사각형 시료에서의 Hall effect. 평형 상태에서 움직이는 charge carrier에 작용하는 Lorentz force $F_L$은 Hall effect에 의한 electric field로 인한 electrical force $F_e$와 균형을 이룬다.](placeholder_fig1.png)

### 2.2 Hall Coefficient

약한 magnetic field에서의 평형 조건에서 Hall coefficient $R_H$는 charge density (carrier concentration)와 electron 및 hole의 mobility의 함수로 표현할 수 있다:

$$R_H = \frac{1}{e_0} \cdot \frac{p \cdot \mu_p^2 - n \cdot \mu_n^2}{(p \cdot \mu_p + n \cdot \mu_n)^2} \tag{II}$$

여기서 각 기호의 의미는 다음과 같다:

| 기호 | 의미 |
|------|------|
| $e_0 = 1.602 \times 10^{-19}$ As | elementary charge |
| $p = p_E + p_S$ | total density of holes |
| $p_E$ | density of holes (intrinsic conduction) |
| $p_S$ | density of holes (hole conduction due to p-doping) |
| $n = n_E$ | density of electrons (intrinsic conduction) |
| $\mu_p$ | mobility of holes |
| $\mu_n$ | mobility of electrons |

식 (II)로부터 다음을 알 수 있다: 전류 $I$와 magnetic field $B$의 방향을 알고 있으면, Hall coefficient $R_H$의 부호로부터 **predominant charge carrier의 극성**을 판별할 수 있다. 또한, 도체 시료가 얇을수록 Hall voltage가 높아진다.

### 2.3 p-Doping과 Extrinsic Conduction

Germanium crystal lattice에 B, Al, In, Ga 등의 Group III 원소를 도핑하면 valence band에 양전하를 띤 hole이 생성된다 (Fig. 2 참조).

![Fig. 2: Extrinsic conduction(왼쪽)과 intrinsic conduction(오른쪽)의 간략화된 다이어그램. Electric field E의 영향 하에서, dopant(acceptor A)를 crystal lattice에 도입하면 valence band(VB)에 hole이라 불리는 양의 charge carrier가 생성된다. 온도가 증가하면 valence electron의 thermal energy가 증가하여 energy gap $E_g$를 넘어 conduction band(CB)로 이동할 수 있게 되며, valence band에 hole이 남게 된다.](placeholder_fig2.png)

이들 dopant의 activation energy $E_A$는 약 **0.01 eV**로, thermal activation에 의해 electron과 hole을 생성하는 데 필요한 activation energy $E_g$ (band gap)보다 현저히 작다. 상온에서 p-doped germanium에서는 dopant에 의한 hole density $p_S$가 intrinsic charge carrier ($p_E$ 및 $n_E$)의 density보다 지배적일 수 있다.

### 2.4 Charge Carrier Density의 결정

Charge transport가 주로 dopant에 의한 hole에 의해 이루어지는 경우 ($n = n_E = p_E \approx 0$), 전류의 함수로 Hall voltage $U_H$를 측정하여 hole density $p_S$를 결정할 수 있다. 식 (I)과 (II)로부터:

$$p_S = \frac{B}{e_0 \cdot d \cdot \frac{U_H}{I}} \tag{III}$$

### 2.5 Mobility

Mobility는 charge carrier와 crystal lattice 사이의 상호작용을 나타내는 척도이다. p-doped germanium의 경우, dopant(acceptor)에 의해 생성된 hole의 mobility $\mu_p$는 다음과 같이 정의된다:

$$\mu_p = \frac{v_p}{E} \tag{IV}$$

여기서 $v_p$는 drift velocity이고, $E$는 voltage drop에 의한 electric field이다.

Electric field $E$는 voltage drop $U$와 p-doped germanium 시료의 길이 $w$로부터 결정된다:

$$E = \frac{U}{w} \tag{V}$$

Drift velocity $v_p$는 Lorentz force가 Hall field에 의한 electrical force와 평형을 이루는 조건에서 결정된다 (Fig. 1 참조):

$$e_0 \cdot v_d \cdot B = e_0 \cdot E_H \tag{VI}$$

이를 $U_H = b \cdot E_H$ 관계를 이용하여 표현하면:

$$v_d = \frac{U_H}{b \cdot B} \tag{VII}$$

식 (V)와 (VII)을 식 (IV)에 대입하면, 상온에서 hole의 mobility $\mu_p$를 다음과 같이 추정할 수 있다:

$$\mu_p = \frac{U_H \cdot w}{b \cdot B \cdot U} \tag{VIII}$$

### 2.6 반도체에서의 전류

반도체 결정에서 전류 $I$는 hole current와 electron current 모두로 구성된다 (Fig. 1 참조):

$$I = b \cdot d \cdot e_0 \cdot (p \cdot v_p + n \cdot v_n) \tag{IX}$$

Charge carrier density는 dopant 농도와 온도에 따라 달라진다. p-doped germanium에서는 세 가지 영역을 구분할 수 있다:

1. **매우 낮은 온도:** Valence band의 electron이 acceptor level로 여기되는 것이 charge carrier의 유일한 원천이다. Hole density $p_S$가 온도에 따라 증가한다.
2. **중간 온도 (Extrinsic conduction 영역):** 모든 acceptor level이 점유되어 $p_S$가 온도에 무관하게 된다. 이 영역에서 intrinsic charge carrier에 의한 charge transport는 무시할 수 있다.
3. **높은 온도:** Valence band에서 conduction band로의 직접적인 thermal excitation이 발생한다. Intrinsic conduction에 의한 charge transport가 증가하여 최종적으로 지배적이 된다.

---

## 3. 장치 (Apparatus)

| 장치 | 모델 번호 | 수량 |
|------|----------|------|
| Base unit for Hall effect Ge | 586 850 | 1 |
| p-doped Ge plug-in board | 586 852 | 1 |
| Combi B-Sensor S | 524 0381 | 1 |
| Extension cable, 15-pole | 501 11 | 1 |
| Sensor CASSY | 524 010 | 1 |
| CASSY Lab | 524 200 | 1 |
| AC/DC Power supply 0~15 V, 5 A | 521 501 | 2 |
| DC Power Supply 0~16 V, 0~5 A | 521 545 | 1 |
| DC power supply | 521 541 | 1 |
| U-core with yoke | 562 11 | 1 |
| Pair of bored pole pieces | 560 31 | 1 |
| Coil with 250 turns | 562 13 | 2 |
| Stand rod, 25 cm | 300 41 | 1 |
| Leybold Multi clamp | 301 01 | 1 |
| Stand base, V-shape, 20 cm | 300 02 | 1 |
| Pair of cables, 1 m, red and blue | 501 46 | 7 |

추가 필요 장비: CASSY Lab이 설치된 PC (Windows 95/98/NT 이상)

---

## 4. 셋업 (Setup)

### 4.1 Plug-in board 장착 및 연결

1. p-doped Ge 결정이 들어 있는 plug-in board를 Base unit for Hall effect의 DIN socket에 핀이 구멍에 맞물릴 때까지 삽입한다.
2. DIN plug가 달린 plug-in board를 조심스럽게 DIN socket에 삽입한다. Rod가 달린 base unit를 U-core의 구멍에 끝까지 삽입하고, plug-in board가 U-core와 평행하게 놓이도록 확인한다 (Base unit 586 850 설명서 참조).
3. Pair of bored pole pieces에 additional pole piece를 부착하고, additional pole piece를 plug-in board의 spacer까지 밀어 넣는다 (plug-in board가 휘지 않도록 주의).
4. Current-controlled power supply의 current limiter를 왼쪽 끝까지 돌린 뒤 전원을 연결한다.

### 4.2 Magnetic Field 측정

- B-probe를 Stand rod를 이용하여 Stand base, V-shape에 고정한다.
- 장치 조정이 완료된 후, magnetic field $B$를 측정하기 전에 B-probe를 gap 사이에 조심스럽게 배치한다 (Base unit 586 850 설명서 참조).
- 측정을 위해 B-probe를 Extension cable을 사용하여 Sensor CASSY에 연결한다.

> **Tip:** Electromagnet을 이용해 magnetic field를 만드는 실험이므로, electromagnet에 흐르는 전류와 magnetic field의 **calibration curve**를 한 번 만들어 두면, 이후에는 magnetic field를 매번 직접 측정하지 않아도 된다.

### 4.3 Hall Voltage 보상 (Compensation)

일정한 전류 $I$로 측정을 수행하기 전에, $B = 0$ T에서 Hall voltage를 보상해야 한다:

1. 전류 $I$ 측정을 위해 케이블을 Sensor CASSY의 **Input A**에 연결한다 (Fig. 3 참조, Base unit 586 850 설명서도 참조).
2. Hall voltage $U_H$ 측정을 위해 케이블을 Sensor CASSY의 **Input B**에 연결한다 (Fig. 3 참조).
3. Cross-current $I$를 최대값으로 설정한 뒤, compensation을 켜고 compensation knob를 사용하여 Hall voltage $U_H$를 영점 조정한다.

### 4.4 Voltage drop 측정

- Voltage drop $U$ 측정을 위해 케이블을 Sensor CASSY의 **Input B**에 연결한다 (Base unit 586 850 설명서의 온도 함수 conductivity 측정 부분 참조).
- 전류 $I$ 측정을 위해 케이블을 Sensor CASSY의 **Input A**에 연결한다.
- 전류 $I$를 최대값으로 설정하고 voltage drop $U$를 측정한다.

![Fig. 3: 전류 I의 함수로 Hall voltage를 측정하기 위한 experimental setup (wiring diagram)](placeholder_fig3_wiring.png)

---

## 5. 안전 주의사항

> **Ge 결정은 매우 깨지기 쉽다:**
> - Plug-in board를 조심스럽게 다루고, 기계적 충격이나 하중을 가하지 않는다.
> - 회로판의 부품이 떨어져 나갈 우려가 있으므로 취급 및 보관에 유의한다.

> **p-doped Ge 결정은 cross-current만 가해도 발열한다:**
> - **p-Ge 및 n-Ge board:** cross-current $I = 33$ mA를 절대 초과하지 않는다.
> - **Ge board (undoped):** cross-current $I = 4$ mA를 절대 초과하지 않는다.
> - Base unit의 cross-current control knob를 왼쪽 끝까지 돌려놓은 상태에서 시작한다.
> - 회로가 뜨거울 수 있으므로 회로 부분을 손으로 만지지 않는다.

> **Electromagnet 관련:**
> - 두 개의 coil에 전류가 흐르며 magnetic field가 생성된다. 두 coil의 magnetic field가 상쇄되도록 연결하면 반도체 Hall bar에 magnetic field가 생성되지 않으므로, 이 경우 연결 상태를 바꾸어야 한다.
> - 100 mT 이상의 magnetic field를 얻을 수 있어야 회로가 제대로 구성된 것이다.

> **CASSY Lab 관련:**
> - Magnetic field 및 Hall voltage 측정의 범위를 적절히 설정한다. 범위가 너무 넓으면 데이터가 digitize되고, 너무 좁으면 원하는 범위를 측정하지 못한다.

---

## 6. 실험 절차 (Carrying out the Experiment)

### 6.1 실험 a) — 전류의 함수로 Hall voltage 측정

1. 먼저 Hall voltage를 보상한다 (4.3절 참조).
2. Magnetic field $B$를 원하는 값으로 설정하고, magnetic flux density $B$를 측정한다.
3. 전류를 최대값으로 설정하고 voltage drop $U$를 측정한다.
4. Hall voltage $U_H$ (Sensor CASSY Input B)를 전류 $I$ (Sensor CASSY Input A)의 함수로 측정한다.
5. 케이블 연결 후 CASSY Lab에서 매개변수를 설정한다.
6. Manual measuring mode에서 측정 버튼 또는 F9를 사용하여 측정한다.
7. 측정 결과를 저장한다.

### 6.2 실험 b) — Magnetic field의 함수로 Hall voltage 측정

1. 먼저 Hall voltage를 보상한다 (4.3절 참조).
2. 전류 $I$를 원하는 값으로 설정한다.
3. Hall voltage $U_H$ (Sensor CASSY Input B)를 magnetic field $B$ (Sensor CASSY Input A)의 함수로 측정한다.
4. 케이블 연결 후 CASSY Lab에서 매개변수를 설정한다.
5. Manual measuring mode에서 측정 버튼 또는 F9를 사용하여 측정한다.
6. 측정 결과를 저장한다.

> **데이터 처리 관련:** 단순히 모니터 화면을 캡처하여 데이터로 사용하지 말고, 측정된 데이터 테이블을 메모장이나 엑셀로 복사하여 직접 그래프를 그려보고 분석한다.

---

## 7. 추가 실험

p-Ge 외에 n-Ge, Ge (undoped) board가 함께 제공된다. 회로를 교체하여 동일한 실험을 수행해 보고, 문제가 있을 경우 원인을 찾아본다.

---

## 8. 측정 예시 (Measuring Example)

### 8.1 실험 a) — 전류의 함수로 Hall voltage

![Fig. 4: 서로 다른 magnetic field에서 전류 I의 함수로 나타낸 Hall voltage $U_H$. 직선은 식 (I)에 따른 fit 결과에 해당한다.](placeholder_fig4.png)

측정 조건:

- 전류: $I = 30$ mA
- Voltage drop: $U = 1.4$ V

### 8.2 실험 b) — Magnetic field의 함수로 Hall voltage

![Fig. 5: $I = 30$ mA에서 magnetic field B의 함수로 나타낸 Hall voltage $U_H$. 기울기 A를 가진 직선은 식 (I)에 따른 fit 결과에 해당한다.](placeholder_fig5.png)

---

## 9. 평가 및 결과 (Evaluation and Results)

### 9.1 실험 a) — 전류의 함수로 Hall voltage

예를 들어 $B = 0.35$ T, $I = 30$ mA인 Fig. 4의 측정에서, 원점을 지나는 직선 fit (CASSY Lab에서 다이어그램 우클릭 → "fit function")을 수행하면 기울기

$$A = \frac{R_H \cdot B}{d} = 2.13 \;\frac{\text{V}}{\text{A}}$$

을 얻는다. 이 linear regression 결과와 식 (III)을 사용하여 extrinsic conduction 영역에서의 hole density $p_S$를 다음과 같이 결정할 수 있다:

$$d = 1 \times 10^{-3} \;\text{m}$$
$$B = 0.35 \;\text{T}$$

$$p_S = \frac{B}{e_0 \cdot d \cdot A} = 1.1 \times 10^{21} \;\frac{1}{\text{m}^3}$$

상온에서의 실험 결과와 p-doped germanium 시료의 치수를 이용하여:

| 매개변수 | 값 |
|---------|-----|
| $U$ (voltage drop) | 1.4 V |
| $B$ (magnetic field) | 0.35 T |
| $U_H$ (Hall voltage) | 72 mV |
| $b$ (시료 높이) | 10 mm |
| $w$ (시료 길이) | 20 mm |

drift velocity $v_p$ (식 (VII))와 mobility $\mu_p$ (식 (VIII))를 추정할 수 있다:

$$v_p = \frac{U_H}{b \cdot B} = 21 \;\frac{\text{m}}{\text{s}}$$

$$\mu_p = \frac{U_H \cdot w}{b \cdot B \cdot U} = 2940 \;\frac{\text{cm}^2}{\text{V·s}}$$

### 9.2 실험 b) — Magnetic field의 함수로 Hall voltage

원점을 지나는 직선의 linear regression으로부터, Hall voltage $U_H$가 magnetic field $B$에 비례함을 알 수 있다:

$$U_H \propto B$$

실험 a)의 결과 ($U_H \propto I$)와 합치면 다음 관계를 얻는다:

$$U_H \propto I \cdot B$$

이는 두께 $d$인 strip-shaped conductor에 대해 이론적으로 유도된 Hall voltage 공식 (식 (I))을 확인해 준다.

Fig. 5의 실험 데이터에 대해 직선 fit을 수행하면 Hall coefficient $R_H$를 다음과 같이 얻는다:

$$d = 1 \times 10^{-3} \;\text{m}$$
$$I = 30 \;\text{mA}$$
$$A = 0.199 \;\text{V/T} \quad (\text{Fig. 5의 기울기})$$

$$R_H = \frac{A \cdot d}{I} = 6.6 \times 10^{-3} \;\frac{\text{m}^3}{\text{As}}$$

금속 도체인 silver의 Hall coefficient ($R_H = 8.9 \times 10^{-11}$ m³/(As))와 비교하면, 반도체의 Hall coefficient가 약 $10^7$배 더 크다는 것을 확인할 수 있다.

---

## 10. 보고서 작성 가이드 (Results & Discussion)

### 10.1 보고서에 포함할 실험 결과

#### Calibration Curve

Electromagnet에 흐르는 전류 vs magnetic field $B$의 calibration curve를 작성하여 포함한다.

#### 실험 a) — $U_H$ vs $I$ ($B$ = const.)

- 여러 magnetic field 값 (예: $B$ = 0.1 T, 0.2 T, 0.35 T)에서 전류 $I$를 변화시키며 측정한 $U_H$ vs $I$ 그래프를 작성한다.
- 각 $B$ 값에 대해 원점을 지나는 linear fit을 수행하고 기울기 $A = R_H \cdot B / d$를 구한다.
- 다음 물리량을 산출한다:

| 물리량 | 산출 방법 | 매뉴얼 참고값 |
|--------|----------|-------------|
| Hole density $p_S$ | $p_S = \frac{B}{e_0 \cdot d \cdot A}$ (식 III) | $1.1 \times 10^{21}$ m$^{-3}$ |
| Drift velocity $v_p$ | $v_p = \frac{U_H}{b \cdot B}$ (식 VII) | 21 m/s |
| Mobility $\mu_p$ | $\mu_p = \frac{U_H \cdot w}{b \cdot B \cdot U}$ (식 VIII) | 2940 cm²/(V·s) |

- Voltage drop $U$도 별도로 기록한다 (매뉴얼 예시: $I$ = 30 mA일 때 $U$ = 1.4 V).

#### 실험 b) — $U_H$ vs $B$ ($I$ = const.)

- 일정한 전류 (예: $I$ = 30 mA)에서 magnetic field $B$를 변화시키며 측정한 $U_H$ vs $B$ 그래프를 작성한다.
- 원점을 지나는 linear fit을 수행하고 기울기 $A$로부터 Hall coefficient를 산출한다:

| 물리량 | 산출 방법 | 매뉴얼 참고값 |
|--------|----------|-------------|
| Hall coefficient $R_H$ | $R_H = \frac{A \cdot d}{I}$ | $6.6 \times 10^{-3}$ m³/(As) |

#### 추가 실험 — n-Ge, undoped Ge board

- n-Ge 및 undoped Ge board에 대해서도 동일한 측정을 수행하고 결과를 포함한다.

### 10.2 Discussion에서 다루어야 할 항목

#### (1) $U_H \propto I \cdot B$ 관계 확인

실험 a)에서 $U_H \propto I$, 실험 b)에서 $U_H \propto B$를 각각 확인했으므로, 이를 종합하면 $U_H \propto I \cdot B$가 성립하며 이론식 (I)이 실험적으로 검증되었음을 논의한다.

#### (2) Hall Coefficient의 크기 비교

측정한 $R_H \sim 10^{-3}$ m³/(As)를 금속 도체 (예: silver의 $R_H = 8.9 \times 10^{-11}$ m³/(As))와 비교한다. 반도체의 Hall coefficient가 약 $10^7$배 더 큰 이유를 carrier concentration의 차이로 설명한다. 금속은 free electron density가 $\sim 10^{28}$ m$^{-3}$인 반면, doped semiconductor는 $\sim 10^{21}$ m$^{-3}$ 수준이므로 $R_H \approx 1/(e_0 \cdot p_S)$에서 큰 차이가 발생한다.

#### (3) 측정된 $p_S$와 $\mu_p$의 타당성

- 측정된 hole density $p_S \sim 10^{21}$ m$^{-3}$가 p-doped Ge의 전형적인 dopant concentration 범위에 부합하는지 논의한다.
- 측정된 mobility $\mu_p \sim 2940$ cm²/(V·s)를 germanium의 문헌값 (hole mobility $\sim 1900$ cm²/(V·s) at 300 K for pure Ge)과 비교하고, doping 농도와 온도에 따른 차이를 논의한다.

#### (4) Hall Voltage Compensation의 필요성

$B = 0$일 때 $U_H \neq 0$인 offset이 발생할 수 있는 원인을 논의한다. Hall voltage 측정용 contact의 기하학적 비대칭으로 인해 전류 경로 상의 등전위선에 정확히 놓이지 않으면 ohmic voltage drop이 Hall voltage에 겹쳐 나타난다. 이를 제거하기 위한 compensation 과정의 중요성을 설명한다.

#### (5) 오차 요인 분석

- **Magnetic field 균일성:** Pole piece 사이 gap에서의 field 균일도가 시료 전체에 걸쳐 일정한지 여부
- **온도 효과:** Cross-current에 의한 Joule heating으로 시료 온도가 상승하면 intrinsic carrier가 증가하여 extrinsic 가정 ($n \approx 0$)이 깨질 수 있음
- **Contact resistance:** 시료와 lead 사이의 접촉 저항이 voltage drop $U$ 측정에 미치는 영향
- **Digitization:** CASSY Lab의 측정 범위 설정이 부적절할 경우 데이터 resolution 저하

#### (6) Charge Carrier 극성 판별

Hall voltage의 부호로부터 predominant charge carrier가 hole임을 확인한다. 전류 방향과 magnetic field 방향을 알고 있을 때, Lorentz force의 방향과 Hall field의 방향이 p-type에 대한 예측과 일치하는지 논의한다.

#### (7) 추가 실험 — n-Ge, undoped Ge board 비교 및 문제점 분석

**n-Ge board:**

- p-Ge와 동일한 실험을 수행했을 때, Hall voltage의 **극성이 반전**됨을 확인한다. 이는 predominant charge carrier가 hole이 아닌 electron임을 의미하며, Hall coefficient $R_H < 0$이 되는 것과 일치한다.
- 측정된 $R_H$로부터 electron density $n_S$를 구하고, p-Ge의 $p_S$와 비교하여 doping 농도 차이를 논의한다.
- Electron mobility $\mu_n$을 구하고, hole mobility $\mu_p$보다 큰지 확인한다. Germanium에서는 일반적으로 $\mu_n > \mu_p$인데, 이는 conduction band의 effective mass가 valence band보다 작기 때문이다.

**Undoped Ge board:**

- Cross-current 제한이 **4 mA**로 매우 낮다는 점에 주의한다 (p-Ge, n-Ge는 33 mA).
- Hall voltage가 거의 관찰되지 않거나 매우 작을 수 있다. 이는 undoped Ge에서 intrinsic carrier만 존재하여 $p_E \approx n_E$이고, 식 (II)에서 $p\mu_p^2$과 $n\mu_n^2$이 서로 상쇄되어 $R_H \approx 0$에 가까워지기 때문이다.
- 만약 약간의 Hall voltage가 관찰된다면, $\mu_n > \mu_p$이므로 $n\mu_n^2 > p\mu_p^2$이 되어 $R_H < 0$ (n-type과 같은 부호)이 나타날 수 있음을 논의한다.

**문제점 분석:**

매뉴얼에서 "문제가 있을 경우 문제가 무엇인지 찾아보자"라고 명시하고 있으므로, 실험 중 발생한 문제 (예: signal-to-noise ratio 부족, 시료 발열, 측정 범위 설정 어려움 등)를 구체적으로 기술하고 원인을 분석해야 한다.

---

## 11. 보충 정보

Hall effect는 1879년에 발견되었다. Hall effect는 모든 도전성 물질에 존재하지만, 반도체 기술이 발전하고 다양한 III-V 화합물이 개발되기 전까지는 실험실 수준의 현상에 머물렀다. 반도체 기술의 발전으로 이전 물질보다 수 자릿수 더 큰 Hall voltage를 생성할 수 있게 되었으며, 기술적 응용에서 반도체의 Hall effect는 특히 **magnetic measurement probe**에 널리 사용되고 있다.

---

## 부록 A: Hall Coefficient 유도 (Derivation of Hall Coefficient)

본 부록에서는 본문 식 (II)의 Hall coefficient 표현식을 단계별로 유도한다.

### A.1 상황 설정

Magnetic field $\mathbf{B} = B\hat{z}$가 z방향으로 걸려 있고, 전류는 x방향으로 흐르는 직사각형 반도체 시료를 고려한다. 시료 내에는 density $p$인 hole(양전하)과 density $n$인 electron(음전하)이 모두 존재한다.

### A.2 각 Charge Carrier에 대한 운동 방정식

Drude model에서, steady state에서의 각 charge carrier의 운동 방정식은 electric force, Lorentz force, 그리고 lattice scattering에 의한 damping의 균형으로 주어진다.

**Hole (+$e_0$):**

$$e_0(\mathbf{E} + \mathbf{v}_p \times \mathbf{B}) - \frac{e_0}{\mu_p}\mathbf{v}_p = 0$$

**Electron (−$e_0$):**

$$-e_0(\mathbf{E} + \mathbf{v}_n \times \mathbf{B}) - \frac{e_0}{\mu_n}\mathbf{v}_n = 0$$

여기서 $\frac{e_0}{\mu}$ 항은 lattice scattering에 의한 damping을 나타내며, mobility의 정의 $\mu = \frac{e_0 \tau}{m^*}$로부터 유도된다.

### A.3 성분별 전개 (Weak Magnetic Field Approximation)

$\mathbf{B} = B\hat{z}$이므로, $\mathbf{v} \times \mathbf{B}$의 x, y 성분은 각각 $v_y B$, $-v_x B$가 된다. 운동 방정식을 x, y 성분으로 분해하고, **weak magnetic field approximation** ($\mu B \ll 1$)에서 2차 보정항을 무시하면:

**Hole의 drift velocity:**

$$v_{px} \approx \mu_p E_x + \mu_p^2 B \, E_y$$

$$v_{py} \approx \mu_p E_y - \mu_p^2 B \, E_x$$

**Electron의 drift velocity:**

$$v_{nx} \approx -\mu_n E_x + \mu_n^2 B \, E_y$$

$$v_{ny} \approx -\mu_n E_y - \mu_n^2 B \, E_x$$

Electron은 음전하이므로 electric field 반대 방향으로 drift하며, Lorentz force의 방향도 hole과 다르게 나타난다.

### A.4 Current Density 계산

총 current density는 hole current와 electron current의 합이다:

$$\mathbf{J} = e_0 \, p \, \mathbf{v}_p + (-e_0) \, n \, \mathbf{v}_n = e_0(p \, \mathbf{v}_p - n \, \mathbf{v}_n)$$

**y방향 current density:**

$$J_y = e_0(p \cdot v_{py} - n \cdot v_{ny})$$

A.3의 결과를 대입하면:

$$J_y = e_0 \left[ p(\mu_p E_y - \mu_p^2 B \, E_x) - n(-\mu_n E_y - \mu_n^2 B \, E_x) \right]$$

$$J_y = e_0 \, E_y (p\mu_p + n\mu_n) - e_0 \, B \, E_x (p\mu_p^2 - n\mu_n^2)$$

**x방향 current density** (weak magnetic field approximation에서 $E_y$ 관련 항이 작으므로):

$$J_x \approx e_0 \, E_x (p\mu_p + n\mu_n)$$

### A.5 Hall Condition 적용

Hall effect의 핵심 조건은 **y방향으로 net current가 흐르지 않는다**는 것이다:

$$J_y = 0$$

이를 $E_y$에 대해 풀면:

$$e_0 \, E_y (p\mu_p + n\mu_n) = e_0 \, B \, E_x (p\mu_p^2 - n\mu_n^2)$$

$$E_y = \frac{p\mu_p^2 - n\mu_n^2}{p\mu_p + n\mu_n} \cdot B \cdot E_x$$

이 $E_y$가 바로 **Hall field**이다.

### A.6 Hall Coefficient 도출

Hall coefficient는 다음과 같이 정의된다:

$$R_H \equiv \frac{E_y}{J_x \cdot B}$$

A.4의 $J_x$와 A.5의 $E_y$를 대입하면:

$$R_H = \frac{\dfrac{p\mu_p^2 - n\mu_n^2}{p\mu_p + n\mu_n} \cdot B \cdot E_x}{e_0 \, E_x (p\mu_p + n\mu_n) \cdot B}$$

$B \cdot E_x$가 약분되어 최종적으로:

$$\boxed{R_H = \frac{1}{e_0} \cdot \frac{p\mu_p^2 - n\mu_n^2}{(p\mu_p + n\mu_n)^2}}$$

이것이 본문의 **식 (II)** 이다.

### A.7 물리적 의미 및 특수한 경우

**Predominant charge carrier의 극성 판별:**

- **p-type 지배** ($p\mu_p^2 > n\mu_n^2$): $R_H > 0$ → hole이 predominant charge carrier
- **n-type 지배** ($n\mu_n^2 > p\mu_p^2$): $R_H < 0$ → electron이 predominant charge carrier

**부호 반전 조건:**

$$p \cdot \mu_p^2 = n \cdot \mu_n^2 \quad \Rightarrow \quad R_H = 0$$

이 조건은 온도가 증가하여 intrinsic charge carrier가 증가할 때 관찰될 수 있다. Hole과 electron이 같은 방향의 Lorentz force를 받지만, 반대 부호의 전하를 가지므로 Hall field에 대한 기여가 반대이기 때문에 서로 상쇄될 수 있다.

**Extrinsic conduction 영역의 단순화** ($n \approx 0$):

Intrinsic charge carrier를 무시할 수 있는 영역에서는 $n = n_E = p_E \approx 0$이므로:

$$R_H \approx \frac{1}{e_0 \cdot p_S}$$

따라서:

$$U_H = R_H \cdot \frac{I \cdot B}{d} = \frac{I \cdot B}{e_0 \cdot p_S \cdot d}$$

이를 $p_S$에 대해 정리하면 본문의 **식 (III)** 을 얻는다:

$$p_S = \frac{B}{e_0 \cdot d \cdot \dfrac{U_H}{I}}$$

---

## 참고문헌 (References)

[1] N.W. Ashcroft and N.D. Mermin, *Solid State Physics*, Ch. 1 & 3, Harcourt (1976).

[2] C. Kittel, *Introduction to Solid State Physics*, 8th ed., Ch. 6, Wiley (2005).

[3] B.G. Streetman and S.K. Banerjee, *Solid State Electronic Devices*, 7th ed., Pearson (2015).

[4] S.M. Sze and K.K. Ng, *Physics of Semiconductor Devices*, 3rd ed., Wiley (2007).

### BibTeX

```bibtex
@book{ashcroft1976,
  author    = {Ashcroft, Neil W. and Mermin, N. David},
  title     = {Solid State Physics},
  publisher = {Harcourt College Publishers},
  year      = {1976},
  address   = {New York}
}

@book{kittel2005,
  author    = {Kittel, Charles},
  title     = {Introduction to Solid State Physics},
  edition   = {8th},
  publisher = {John Wiley \& Sons},
  year      = {2005},
  address   = {Hoboken, NJ}
}

@book{streetman2015,
  author    = {Streetman, Ben G. and Banerjee, Sanjay Kumar},
  title     = {Solid State Electronic Devices},
  edition   = {7th},
  publisher = {Pearson},
  year      = {2015},
  address   = {Upper Saddle River, NJ}
}

@book{sze2007,
  author    = {Sze, Simon M. and Ng, Kwok K.},
  title     = {Physics of Semiconductor Devices},
  edition   = {3rd},
  publisher = {John Wiley \& Sons},
  year      = {2007},
  address   = {Hoboken, NJ}
}
```
