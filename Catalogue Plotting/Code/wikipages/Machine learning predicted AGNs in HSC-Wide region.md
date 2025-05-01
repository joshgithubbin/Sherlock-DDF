**Authors:** Hsieh B.-C., Wang W.-H., Lin Y.-T., Lim C.-F., Toba Y.,, Zhong Y.,Chang S.-Y., <Astrophys. J., 920, 68 (2021)>, =2021ApJ...920...68C

## Summary: Machine learning predicted AGNs in HSC-Wide region 

We investigate the performance of machine-learning techniques in classifying active galactic nuclei (AGNs), including X-ray-selected AGNs (XAGNs), infrared-selected AGNs (IRAGNs), and radio-selected AGNs (RAGNs). Using the known physical parameters in the Cosmic Evolution Survey (COSMOS) field, we are able to create quality training samples in the region of the Hyper Suprime-Cam (HSC) survey. We compare several Python packages (e.g., scikit- learn, Keras, and XGBoost) and use XGBoost to identify AGNs and show the performance (e.g., accuracy, precision, recall, F1 score, and AUROC). Our results indicate that the performance is high for bright XAGN and IRAGN host galaxies. The combination of the HSC (optical) information with the Wide-field Infrared Survey Explorer band 1 and band 2 (near-infrared) information performs well to identify AGN hosts. For both type 1 (broad-line) XAGNs and type 1 (unobscured) IRAGNs, the performance is very good by using optical-to-infrared information. These results can apply to the five-band data from the wide regions of the HSC survey and future all-sky surveys.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-920-68/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>table7.dat</summary>

| Bytes   | Format   | Units      | Label   | Explanations                                       |
|:--------|:---------|:-----------|:--------|:---------------------------------------------------|
| 1- 17   | I17      | ---        | ID      | objid in HSC-SSP PDR2 (1)                          |
| 19- 27  | F9.5     | deg        | RAdeg   | [149/152] Right ascension HSC-SSP PDR2 (J2000) (1) |
| 29- 35  | F7.5     | deg        | DEdeg   | [1/4] declination in HSC-SSP PDR2 (J2000) (1)      |
| 37- 37  | I1       | ---        | XAGN    | [0/1] 1: X-ray selected AGNs predicted by ML       |
| 39- 39  | I1       | ---        | IRAGN   | [0/1] 1: Infrared selected AGNs predicted by ML    |
| 41- 41  | I1       | ---        | RAGN    | [0/1] 1: Radio selected AGNs predicted by ML       |
| 43- 49  | F7.5     | ---        | XAGNp   | [0.009/0.97] Probability of X-ray selected AGNs    |
| 51- 57  | F7.5     | ---        | IRAGNp  | [0.01/0.97] Probability of Infrared selected AGNs  |
| 59- 65  | F7.5     | ---        | RAGNp   | [0.01/0.91] Probability of Radio selected AGNs     |
| 2       | (S19a    | Wide-layer | data),  | http://hsc.mtk.nao.ac.jp/ssp/                      |

**Note**: Hyper SuprimeCam Subaru Strategic Program Public Data Release 2
    (S19a Wide-layer data), http://hsc.mtk.nao.ac.jp/ssp/

</details>
