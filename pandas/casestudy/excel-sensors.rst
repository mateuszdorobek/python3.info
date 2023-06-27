Excel Sensors
=============
* Working with Excel (file, spreadsheet)
* Selecting data
* Binary classification


Todo
----
1. zaczytać dane z Excel (plik, arkusz)
2. Wybrać odpowiednie dane (Luminance)
3. Wykres aktywności ludzi tego dnia

Zwróć uwagę, że niektóre urządzenia elektroniczne emitują światło (zegarki,
monitory, sprzęt laboratoryjny) jednak nie jest oznaka tego, że zespół jest
aktywny. Aktywność jest wtedy, gdy oświetlenie jest powyżej *jakiegoś* poziomu
(threshold). Poziom ten musimy określić na podstawie obserwacji danych.

Ten poziom oświetlenia poniżej wartości progowej w inżynierii nazywany jest
szumem tła (background noise), są to zakłócenia w danych. Dane najczęściej
nazywamy sygnałem.


Code
----
.. literalinclude:: src/excel-sensors.py
    :language: python


Plots
-----
.. figure:: img/excel-sensors-actinogram.png
.. figure:: img/excel-sensors-activity.png
.. figure:: img/excel-sensors-illuminance.png
