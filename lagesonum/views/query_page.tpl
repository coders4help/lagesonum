% include('views/header.tpl', active='query')

<div class="container">
      <div class="starter-template">

<p>{{_('search_pitch')}}</p>


<form action="{{i18n_path('/query')}}" method="post">
   <input name="number" type="text">
   <input type="submit" value="{{_('submit_label')}}">
</form>

<p>found: <b>{{result}}</b><br>
number of times: {{n}}<br>
from: {{timestamp_first}}<br>
to: {{timestamp_last}}</p>


<h3>{{_('pleasenote_title')}}</h3>
<p>{{_('pleasenote')}}</p>

</div></div>

% include('views/footer.tpl')


