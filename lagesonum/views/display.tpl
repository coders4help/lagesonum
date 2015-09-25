% include('views/header.tpl')

<div class="container">
      <div class="starter-template">

<h2>Live display</h2>

% if numbers is not None:
<p>These numbers have been entered since {{since}} by at least {{min_count}} different helpers.</p>
   {{numbers}}

<p><br>Alphabet order</p>

% else:
<p>No numbers entered since {{since}} more than {{min_count}} times.</p>

<h3>{{_('Bitte beachten:')}}</h3>
<p>{{_(u'Diese Website ist am 22.9.15 an den Start gegangen. Nur Nummern, die seitdem aufgerufen wurden, werden angezeigt.')}}</p>

</div></div>

% include('views/footer.tpl')


