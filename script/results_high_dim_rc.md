High dimension reservoir
================

<script src="results_high_dim_rc_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="results_high_dim_rc_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


# Forecast

## Performance

### Sanity check

![Number of reservoir per day for
prediction](results_high_dim_rc_files/figure-commonmark/sanitycheck-1.png)

### Performance

<table class="table" style="margin-left: auto; margin-right: auto;">
<caption>Model performance</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> short_name_model </th>
   <th style="text-align:right;"> pmutQuant </th>
   <th style="text-align:right;"> pmutCat </th>
   <th style="text-align:right;"> lr_sigma </th>
   <th style="text-align:left;"> update </th>
   <th style="text-align:right;"> AE </th>
   <th style="text-align:right;"> sd_AE </th>
   <th style="text-align:right;"> AE_baseline </th>
   <th style="text-align:right;"> sd_AE_baseline </th>
   <th style="text-align:right;"> RE </th>
   <th style="text-align:right;"> sd_RE </th>
   <th style="text-align:right;"> RE_baseline </th>
   <th style="text-align:right;"> sd_RE_baseline </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.93 </td>
   <td style="text-align:right;"> 13.38 </td>
   <td style="text-align:right;"> -2.65 </td>
   <td style="text-align:right;"> 5.74 </td>
   <td style="text-align:right;"> 0.28 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.90 </td>
   <td style="text-align:right;"> 1.59 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.77 </td>
   <td style="text-align:right;"> 13.14 </td>
   <td style="text-align:right;"> -2.82 </td>
   <td style="text-align:right;"> 5.05 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.87 </td>
   <td style="text-align:right;"> 1.06 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.51 </td>
   <td style="text-align:right;"> 12.87 </td>
   <td style="text-align:right;"> -3.08 </td>
   <td style="text-align:right;"> 5.82 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.88 </td>
   <td style="text-align:right;"> 1.56 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.69 </td>
   <td style="text-align:right;"> 12.54 </td>
   <td style="text-align:right;"> -2.90 </td>
   <td style="text-align:right;"> 5.79 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.85 </td>
   <td style="text-align:right;"> 1.52 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 14.89 </td>
   <td style="text-align:right;"> 12.14 </td>
   <td style="text-align:right;"> -3.70 </td>
   <td style="text-align:right;"> 7.36 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.30 </td>
   <td style="text-align:right;"> 0.84 </td>
   <td style="text-align:right;"> 2.16 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.27 </td>
   <td style="text-align:right;"> 13.11 </td>
   <td style="text-align:right;"> -3.32 </td>
   <td style="text-align:right;"> 5.80 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.88 </td>
   <td style="text-align:right;"> 1.40 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.26 </td>
   <td style="text-align:right;"> 12.94 </td>
   <td style="text-align:right;"> -3.33 </td>
   <td style="text-align:right;"> 7.88 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.31 </td>
   <td style="text-align:right;"> 0.84 </td>
   <td style="text-align:right;"> 1.83 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.016 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.02 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.24 </td>
   <td style="text-align:right;"> 13.02 </td>
   <td style="text-align:right;"> -3.34 </td>
   <td style="text-align:right;"> 7.14 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.87 </td>
   <td style="text-align:right;"> 1.79 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.82 </td>
   <td style="text-align:right;"> 13.10 </td>
   <td style="text-align:right;"> -2.76 </td>
   <td style="text-align:right;"> 5.86 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.90 </td>
   <td style="text-align:right;"> 1.13 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.96 </td>
   <td style="text-align:right;"> 13.24 </td>
   <td style="text-align:right;"> -2.63 </td>
   <td style="text-align:right;"> 5.34 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.36 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.06 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.75 </td>
   <td style="text-align:right;"> 12.97 </td>
   <td style="text-align:right;"> -2.84 </td>
   <td style="text-align:right;"> 5.67 </td>
   <td style="text-align:right;"> 0.28 </td>
   <td style="text-align:right;"> 0.36 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.61 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.67 </td>
   <td style="text-align:right;"> 13.17 </td>
   <td style="text-align:right;"> -2.91 </td>
   <td style="text-align:right;"> 5.07 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.36 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.23 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.32 </td>
   <td style="text-align:right;"> 12.73 </td>
   <td style="text-align:right;"> -3.27 </td>
   <td style="text-align:right;"> 6.50 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.32 </td>
   <td style="text-align:right;"> 0.81 </td>
   <td style="text-align:right;"> 1.65 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.14 </td>
   <td style="text-align:right;"> 12.89 </td>
   <td style="text-align:right;"> -3.45 </td>
   <td style="text-align:right;"> 5.80 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.55 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 14.99 </td>
   <td style="text-align:right;"> 12.23 </td>
   <td style="text-align:right;"> -3.60 </td>
   <td style="text-align:right;"> 7.40 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.82 </td>
   <td style="text-align:right;"> 1.29 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.04 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.04 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.14 </td>
   <td style="text-align:right;"> 12.75 </td>
   <td style="text-align:right;"> -3.44 </td>
   <td style="text-align:right;"> 6.18 </td>
   <td style="text-align:right;"> 0.28 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.68 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.45 </td>
   <td style="text-align:right;"> 12.94 </td>
   <td style="text-align:right;"> -3.13 </td>
   <td style="text-align:right;"> 6.01 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.62 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.76 </td>
   <td style="text-align:right;"> 13.31 </td>
   <td style="text-align:right;"> -2.82 </td>
   <td style="text-align:right;"> 5.51 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.45 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.57 </td>
   <td style="text-align:right;"> 13.06 </td>
   <td style="text-align:right;"> -3.02 </td>
   <td style="text-align:right;"> 6.21 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.13 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.66 </td>
   <td style="text-align:right;"> 13.05 </td>
   <td style="text-align:right;"> -2.93 </td>
   <td style="text-align:right;"> 5.38 </td>
   <td style="text-align:right;"> 0.28 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.67 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.62 </td>
   <td style="text-align:right;"> 12.69 </td>
   <td style="text-align:right;"> -2.97 </td>
   <td style="text-align:right;"> 5.84 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.87 </td>
   <td style="text-align:right;"> 1.56 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.60 </td>
   <td style="text-align:right;"> 13.20 </td>
   <td style="text-align:right;"> -2.99 </td>
   <td style="text-align:right;"> 5.50 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.88 </td>
   <td style="text-align:right;"> 1.36 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 14.94 </td>
   <td style="text-align:right;"> 12.43 </td>
   <td style="text-align:right;"> -3.65 </td>
   <td style="text-align:right;"> 6.71 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.82 </td>
   <td style="text-align:right;"> 1.64 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.1 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.10 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.69 </td>
   <td style="text-align:right;"> 12.99 </td>
   <td style="text-align:right;"> -2.90 </td>
   <td style="text-align:right;"> 5.41 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.89 </td>
   <td style="text-align:right;"> 1.37 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.14 </td>
   <td style="text-align:right;"> 12.80 </td>
   <td style="text-align:right;"> -3.45 </td>
   <td style="text-align:right;"> 6.33 </td>
   <td style="text-align:right;"> 0.28 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.85 </td>
   <td style="text-align:right;"> 1.71 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.1 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.1 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 14.85 </td>
   <td style="text-align:right;"> 12.67 </td>
   <td style="text-align:right;"> -3.73 </td>
   <td style="text-align:right;"> 5.97 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.84 </td>
   <td style="text-align:right;"> 1.17 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.58 </td>
   <td style="text-align:right;"> 13.11 </td>
   <td style="text-align:right;"> -3.01 </td>
   <td style="text-align:right;"> 6.00 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.59 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.2 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.2 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.16 </td>
   <td style="text-align:right;"> 12.69 </td>
   <td style="text-align:right;"> -3.42 </td>
   <td style="text-align:right;"> 5.90 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.85 </td>
   <td style="text-align:right;"> 1.34 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.20 </td>
   <td style="text-align:right;"> 12.85 </td>
   <td style="text-align:right;"> -3.39 </td>
   <td style="text-align:right;"> 7.27 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.84 </td>
   <td style="text-align:right;"> 1.44 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.4 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.4 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.21 </td>
   <td style="text-align:right;"> 13.21 </td>
   <td style="text-align:right;"> -3.37 </td>
   <td style="text-align:right;"> 5.68 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.33 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.44 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> No monthly update </td>
   <td style="text-align:right;"> 15.45 </td>
   <td style="text-align:right;"> 13.07 </td>
   <td style="text-align:right;"> -3.14 </td>
   <td style="text-align:right;"> 6.32 </td>
   <td style="text-align:right;"> 0.26 </td>
   <td style="text-align:right;"> 0.35 </td>
   <td style="text-align:right;"> 0.85 </td>
   <td style="text-align:right;"> 1.12 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> PmutQuant = 0.5 ; PmutCat = 0.25 ; lr sigma = 0.8 </td>
   <td style="text-align:right;"> 0.5 </td>
   <td style="text-align:right;"> 0.25 </td>
   <td style="text-align:right;"> 0.8 </td>
   <td style="text-align:left;"> Monthly update </td>
   <td style="text-align:right;"> 15.50 </td>
   <td style="text-align:right;"> 13.00 </td>
   <td style="text-align:right;"> -3.09 </td>
   <td style="text-align:right;"> 5.34 </td>
   <td style="text-align:right;"> 0.27 </td>
   <td style="text-align:right;"> 0.34 </td>
   <td style="text-align:right;"> 0.86 </td>
   <td style="text-align:right;"> 1.19 </td>
  </tr>
</tbody>
</table>

![](results_high_dim_rc_files/figure-commonmark/tileperf-1.png)

![](results_high_dim_rc_files/figure-commonmark/lineperf-1.png)

# Hyperparameters

## Numeric hyperparameters

![Sanity check leaking rate, variance of leaking rate of genetic
individuals should increase with leaking rate mutation
sigma](results_high_dim_rc_files/figure-commonmark/unnamed-chunk-5-1.png)

![Numeric hyperparameter, density of all genetic
individuals.](results_high_dim_rc_files/figure-commonmark/unnamed-chunk-6-1.png)

![Numeric hyperparameter, density of 40 best genetic individuals per
hyperparameter update
date.](results_high_dim_rc_files/figure-commonmark/unnamed-chunk-7-1.png)

## Categorical hyperparameters

![Number of selected features among the best genetic
individuals.](results_high_dim_rc_files/figure-commonmark/unnamed-chunk-9-1.png)

<!-- ```{r factorialanalysis} -->
<!-- # Loading data -->
<!-- library(FactoMineR) -->
<!-- res.mca <- df_all_hp_best40_qual |>  -->
<!--   filter(last_used_observation == "2021-03-01") |>  -->
<!--   select(pmutCat, lr_sigma, ends_with("_bin")) |>  -->
<!--   mutate(across(.cols = c(pmutCat, lr_sigma), .fns = as.factor)) |>  -->
<!--   MCA(ncp = 200, -->
<!--       quali.sup = c("pmutCat", "lr_sigma"), -->
<!--       graph=FALSE) -->
<!-- res.hcpc <- HCPC(res.mca, graph = FALSE, nb.clust = -1, max = 100, min = 2) -->
<!-- res.hcpc$desc.ind -->
<!-- ``` -->
<!-- ```{r} -->
<!-- library(umap) -->
<!-- df_freq_selection <- df_all_hp_best40_qual |>  -->
<!--   tidyr::pivot_longer(cols = ends_with("_bin")) |>  -->
<!--   group_by(short_name_model,  pmutCat, lr_sigma, last_used_observation, name) |>  -->
<!--   summarise(value = mean(value == "y"), .groups = "drop") |>  -->
<!--   tidyr::pivot_wider() -->
<!-- umap_test <- umap(df_freq_selection |>  -->
<!--   select(ends_with("_bin"))) -->
<!-- umap_test$layout |>  -->
<!--   as.data.frame() |>  -->
<!--   bind_cols(df_freq_selection) |>  -->
<!--   mutate(pmutCat = as.factor(pmutCat), -->
<!--          lr_sigma = as.factor(lr_sigma)) |>  -->
<!--   ggplot(mapping = aes(x = V1, y = V2, color = lr_sigma, shape = pmutCat)) + -->
<!--   geom_point() -->
<!-- ``` -->

![](results_high_dim_rc_files/figure-commonmark/freqselectionfeatures-1.png)
