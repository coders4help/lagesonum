% include('views/header.tpl')

<div class="container">
      <div class="starter-template">

<h2>{{_('display_link')}}</h2>

% if numbers is not None:
<p>{{_('numberdisplaytxt')}}</p>
   {{numbers}}

<p><br>{{_('alphabetorder')}}</p>

% else:
<p>{{_('nonumbersentered')}}</p>

<h3>{{_('pleasenote_title')}}</h3>
<p>{{_(u'pleasenote')}}</p>

</div></div>

% include('views/footer.tpl')


