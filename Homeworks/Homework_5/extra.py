p_0_initial = R_0_1 @ p_1_1
p_0_initial

v_p_0_0 = get_skew(w_0) @ p_0_initial

v_p_0_0

p_0_final = v_p_0_0 * final_time + p_0_initial