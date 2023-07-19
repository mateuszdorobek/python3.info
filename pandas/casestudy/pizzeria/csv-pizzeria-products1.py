import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)



df = (pd
    .read_csv('pizzeria-products1.csv')
    .dropna(how='all', axis='columns')
    .dropna(how='all', axis='rows')
    .iloc[24:-2, [0,6,7,8,10,11,12]]
    .set_axis(['produkt', 'jednostka', 'ilosc', 'vat', 'rodzaj', 'rabat', 'sprzedaz'], axis='columns')
    .assign(sprzedaz=lambda df: pd.to_numeric(df['sprzedaz'], errors='coerce'))
    .dropna()
    .astype({'ilosc':'float32', 'vat':'int8', 'rabat':'int8', 'sprzedaz': 'float64'})
    .convert_dtypes()
    .set_index('produkt', drop=True)
    .round({'sprzedaz': 1})
    .sort_values(by='sprzedaz', ascending=False)
)

#                                          jednostka  ilosc  vat   rodzaj  rabat  sprzedaz
# produkt
# MARGHERITA PIZZA                              szt.    135    8  Potrawa      0    2995.0
# TARTUFATA P                                   szt.     77    8  Potrawa      0    2772.0
# PROSCIUTTO E FUNGHIP                          szt.     70    8  Potrawa      0    1989.0
# CAPRICCIOSA P                                 szt.     60    8  Potrawa      0    1922.0
# DIAVOLA P                                     szt.     76    8  Potrawa      1    1913.0
# OLIO EXTRA SICILIA 0,5L 2022                  szt.     23    0  Potrawa      0    1380.0
# PIZZA PROSCIUTTO COTTO                        szt.     51    8  Potrawa      0    1285.0
# TARTUFATA P_całość                            szt.     28    8  Potrawa      0    1092.0
# MARGHERITA PIZZA DELI                         szt.     31    8  Potrawa      0     850.0
# BUFALA P                                      szt.     23    8  Potrawa      0     833.0
# VEGETARIANA P                                 szt.     33    8  Potrawa      0     825.0
# RUSTICA P                                     szt.     24    8  Potrawa      0     792.0
# 4 FORMAGGI P                                  szt.     22    8  Potrawa      0     770.0
# PIZZA SALAME E FUNGHI                         szt.     26    8  Potrawa      0     728.0
# FUOCO DELL`ETNA P                             szt.     18    8  Potrawa      0     684.0
# NORCINA P                                     szt.     19    8  Potrawa      0     646.0
# PROSCIUTTO E FUNGHIP_całość                   szt.     19    8  Potrawa      0     623.0
# TONNO E CIPOLLA                               szt.     20    8  Potrawa      0     600.0
# NDUJA PIZZA                                   szt.     18    8  Potrawa      0     575.0
# DIAVOLA P_całość                              szt.     18    8  Potrawa      0     549.0
# DA MARIO                                      szt.     14    8  Potrawa      0     532.0
# PIZZA SALAME E FUNGHI_całość                  szt.     14    8  Potrawa      0     460.0
# POLARA LEMONIADA                              szt.     38   23  Potrawa      0     456.0
# VEGETARIANA P_całość                          szt.     14    8  Potrawa      0     428.0
# CALZONE PRO E FUNGHI                          szt.     14    8  Potrawa      0     420.0
# ZOLA E SPINACI BIANC                          szt.     13    8  Potrawa      0     416.0
# SANT`ANTONIO                                  szt.     12    8  Potrawa      0     408.0
# PIZZA SALSICCIA                               szt.     14    8  Potrawa      0     390.0
# CALZONE RUSTICO                               szt.     10    8  Potrawa      0     360.0
# MIMOSA P                                      szt.     13    8  Potrawa      0     356.0
# CAPRICCIOSA P _całość                         szt.     10    8  Potrawa      0     350.0
# PIZZA PROSCIUTTO COTTO_całość                 szt.     12    8  Potrawa      0     336.0
# YOGA MELA                                     szt.     42    5  Potrawa      0     336.0
# CALZONE BOMBA.                                szt.      9    8  Potrawa      0     324.0
# 4 FORMAGGI PD                                 szt.      8    8  Potrawa      0     304.0
# ZOLA E SPINACI ROSSA                          szt.     10    8  Potrawa      0     300.0
# BIANCO 1 L                                    szt.      5   23  Potrawa      0     290.0
# CALZONE TARTUFATO                             szt.      8    8  Potrawa      0     288.0
# RUSTICA P_całość                              szt.      8    8  Potrawa      0     288.0
# PEPSI                                         szt.     33   23  Potrawa      0     264.0
# PIZZA CRUDO_całość                            szt.      8    8  Potrawa      0     262.0
# CALZONE PRO E FUNGHI_całość                   szt.      7    8  Potrawa      0     248.0
# VULCANO P                                     szt.      7    8  Potrawa      0     238.0
# DOSTAWA I SERWIS                              szt.     57   23  Potrawa      0     226.5
# POLARA COLA                                   szt.     18   23  Potrawa      0     216.0
# POLARA ARANCIA ROSSA                          szt.     16   23  Potrawa      0     192.0
# TONNO E NDUJA P                               szt.      5    8  Potrawa      0     190.0
# PIZZA CRUDO                                   szt.      6    8  Potrawa      0     180.0
# ZOLA E SPINACI BIANC_całość                   szt.      5    8  Potrawa      0     178.0
# MARGHERITA BIANCA P                           szt.      7    8  Potrawa      0     175.0
#                                             ...    ...  ...      ...    ...       ...
# VERDE_całość                                  szt.      3    8  Potrawa      0     105.0
# CLASSICO                                      szt.      4    8  Potrawa      0     100.0
# BUFALA P_całość                               szt.      2    8  Potrawa      0     100.0
# APEROL SOUR                                   szt.      4   23  Potrawa      0      96.0
# FOCACCIA                                      szt.      6    8  Potrawa      0      90.0
# DA MARIO_całość                               szt.      2    8  Potrawa      0      82.0
# FUOCO DELL`ETNA P_całość                      szt.      2    8  Potrawa      0      82.0
# CAPRESE.                                      szt.      3    8  Potrawa      0      81.0
# CAFFE LUNGO                                   szt.      9   23  Potrawa      0      81.0
# CALZONE TARTUFATO_całość                      szt.      2    8  Potrawa      0      78.0
# VODKA BOCIAN 0,5                              szt.      1   23  Potrawa      0      75.0
# VULCANO P_całość                              szt.      2    8  Potrawa      0      74.0
# NDUJA PIZZA_całość                            szt.      2    8  Potrawa      0      73.0
# TYKIE 0,3                                     szt.     10   23  Potrawa      0      70.0
# LA FAVORITA LAMBRUSCO                         szt.      2   23  Potrawa      0      70.0
# CZERWONY LAGER                                szt.      6   23  Potrawa      0      66.0
# SAN PELLEGRINO                                szt.      4   23  Potrawa      0      64.0
# ROSSO 150 ML                                  szt.      7   23  Potrawa      0      63.0
# PROSECCO 100 ML                               szt.      5   23  Potrawa      0      60.0
# ACQUA NAT                                     szt.     10   23  Potrawa      0      60.0
# BIANCO 500 ML                                 szt.      2   23  Potrawa      0      58.0
# ROSSO 500 ML                                  szt.      2   23  Potrawa      0      58.0
# CLASSICO _całość                              szt.      2    8  Potrawa      0      56.0
# ESPRESSO                                      szt.      8   23  Potrawa      0      56.0
# FOCACCIA_całość                               szt.      3    8  Potrawa      0      54.0
# A-MANO PRIMITIVO PUGLIA                       szt.      1   23  Potrawa      0      50.0
# ITINERA CHARDONNAY PRIMA CLASSE               szt.      1   23  Potrawa      0      48.0
# INTINERA PRIMA CLASSE MONTEPULCIANO D'AB      szt.      1   23  Potrawa      0      48.0
# POLARA THE PESCA                              szt.      4   23  Potrawa      0      48.0
# PROSECCO INTINERA BRUT DOC                    szt.      1   23  Potrawa      0      45.0
# ACQUA GAS                                     szt.      7   23  Potrawa      0      42.0
# TONNO E NDUJA P_całość                        szt.      1    8  Potrawa      0      41.0
# LECH FREE                                     szt.      5   23  Potrawa      0      40.0
# ESPRESSO DOPPIO                               szt.      3   23  Potrawa      0      36.0
# YOGA MELA_1                                   szt.      4    5  Potrawa      0      36.0
# LA RUSTICA COLLI PIACENTINI BIANCO            szt.      1   23  Potrawa      0      35.0
# TERRE FORTI TREBBIANO- CHARDONNAY RUBICO      szt.      1   23  Potrawa      0      34.0
# PESTO RAGUSANO 180G                           szt.      1    8  Potrawa      0      33.0
# VERDE                                         szt.      1    8  Potrawa      0      32.0
# PIZZA NORMA_całość                            szt.      1    8  Potrawa      0      29.0
# POLARA THE PESCA_1                            szt.      2   23  Potrawa      0      28.0
# POLARA LEMONIADA_1                            szt.      2   23  Potrawa      0      28.0
# PIZZA NORMA                                   szt.      1    8  Potrawa      0      26.0
# FOCACCIA CON RICOTTA                          szt.      1    8  Potrawa      0      22.0
# SUCCO DI MELA 1L                              szt.      1    8  Potrawa      0      20.0
# ACQUA PANNA                                   szt.      1   23  Potrawa      0      16.0
# AAAAA KORKOWE                                 szt.      1   23  Potrawa      0      15.0
# POLARA THE LIMONE_1                           szt.      1   23  Potrawa      0      14.0
# POLARA CHINOTTO_1                             szt.      1   23  Potrawa      0      14.0
# BUFALA 125G                                   szt.      1    5  Potrawa      0      10.0
# [117 rows x 6 columns]
