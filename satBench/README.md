This archive contains instaces encoding partial robustness in team formation. See the following paper for more details: Partial Robustness in Team Formation: Bridging the Gap between Robustness and Resilience (Schwind, Demirović, Inoue, and Lagniez - AAMAS'21).

 - info.txt that report for each instance if it has been solved or not, if it has been solved the running time.
 - BENCH.cnf, 20 CNF instances classifed as follow:
   - 5 easy (<100s by CaDiCaL): ktf_TF-4.tf_2_0.02_18.cnf ktf_TF-5.tf_4_0.06_87.cnf ktf_TF-1.tf_4_0.06_101.cnf ktf_TF-7.tf_3_0.06_113.cnf ktf_TF-3.tf_3_0.02_24.cnf
   - 5 medium (<1500s by CaDiCaL): ktf_TF-6.tf_4_0.06_77.cnf ktf_TF-8.tf_4_0.06_109.cnf ktf_TF-4.tf_4_0.04_35.cnf ktf_TF-6.tf_3_0.02_26.cnf ktf_TF-5.tf_4_0.02_29.cnf
   - 5 hard (<36000s by CaDiCaL): ktf_TF-3.tf_2_0.02_24.cnf ktf_TF-4.tf_4_0.06_52.cnf ktf_TF-1.tf_3_0.04_68.cnf ktf_TF-2.tf_4_0.06_107.cnf ktf_TF-8.tf_4_0.02_37.cnf
   - 5 unsolved (>36000s by CaDiCaL): ktf_TF-6.tf_4_0.04_51.cnf ktf_TF-1.tf_3_0.02_34.cnf ktf_TF-9.tf_2_0.02_40.cnf ktf_TF-3.tf_4_0.04_48.cnf ktf_TF-9.tf_3_0.02_40.cnf