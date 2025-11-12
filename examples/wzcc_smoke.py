import numpy as np
from wplzx.wzcc.quantize import theta_from_triplet_wzcc, snap_phase
from wplzx.wzcc.verify import statevector_from_rz, global_phase_equal, phase_distance

def main():
    # 예: a=8, α=π/4, k=1 → θ = π/2
    a, alpha, k = 8, np.pi/4, 1
    theta = theta_from_triplet_wzcc(a, alpha, k)

    # 노이즈 포함 후 스냅
    theta_noisy = theta + 0.01
    theta_snap = snap_phase(theta_noisy, a)

    # 상태 비교
    psi = statevector_from_rz(theta_noisy)
    phi = statevector_from_rz(theta_snap)

    print("a, alpha, k =", a, alpha, k)
    print("theta      =", theta)
    print("theta_noisy=", theta_noisy)
    print("theta_snap =", theta_snap)
    print("global-phase equal? ", global_phase_equal(psi, phi))
    print("phase distance      =", phase_distance(psi, phi))

if __name__ == "__main__":
    main()
