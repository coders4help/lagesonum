<html><head><title>LAGeSoNUM - see the numbers @ LaGeSo</title></head><body>

<h1>LAGeSoNUM - see the numbers @ LaGeSo, Berlin</h1>
<h2>enter numbers</h2>

<p>Everyone in the queue at LaGeSo: Please enter the currently displayed numbers. This way, people not in front of LaGeSo can check if their number has been called. It will work, if everyone works together! Today you help entering numbers, tomorrow you can profit from others entering numbers. <em>TOGETHER WE CAN DO IT!</em></p>

<form action="/enter" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="Abschicken">
</form>

<img src="pics/anzeigetafel.jpg"/>

<ul>
% for number in entered:
    <li>eingegeben: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

<a href="/">zur Startseite</a>
<a href="impressum.html">Kontakt</a>
</body></html>
