<html><head><title>Numbers @ LaGeSo</title></head><body>

<h1>Numbers @ LaGeSo</h1>

<p><a href="/">[ in German ]</a></p>

<p>الجميع في قائمة الانتظار في LaGeSo: الرجاء إدخال الأرقام المعروضة حاليا. بهذه الطريقة، والناس ليس أمام LaGeSo يمكن معرفة ما اذا كان قد تم استدعاء عددهم. أنه سوف يعمل، إذا كان الجميع يعمل معا! اليوم كنت تساعد إدخال أرقام، وغدا يمكنك الاستفادة من الآخرين إدخال الأرقام. معا يمكننا ان نفعل ذلك!</p>

<form action="/enter" method="post">
   <textarea name="numbers" rows="10" cols="30"></textarea>
   <input type="submit" value="Send">
</form>

<ul>
% for number in entered:
    <li>eingegeben: <b>{{number}}</b> [{{timestamp}}]</li>
  % end
</ul>

<h3><a href="/query">search a number</a></h3>

<p>Impressum</p>

</body></html>