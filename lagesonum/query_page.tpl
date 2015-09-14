
<html><head><title>Numbers @ LaGeSo</title></head><body>


<h1>Numbers @ LaGeSo</h1>
<h3>Search a number</h3>

<form action="{{i18n_path('/query')}}" method="post">
   <input name="number" type="text"></input>
   <input type="submit" value="Abschicken">
</form>

<p>gefunden: <b>{{result}}</b><br>
number of times: {{n}}<br>
from: {{timestamp_first}}<br>
to: {{timestamp_last}}</p>

<a href="{{i18n_path('/')}}">zur Startseite</a>

</body></html>

