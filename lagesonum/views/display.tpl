% include('views/header.tpl')

<div class="container">
      <div class="starter-template">

<p>Live display</p>

% if numbers is not None:
<p>Numbers entered since {{since}} more than {{min_count}} times.</p>
   {{numbers}}

% else:
<p>No numbers entered since {{since}} more than {{min_count}} times.</p>

<h3>{{_('Bitte beachten:')}}</h3>
<p>{{_(u'Diese Website ist am 22.9.15 an den Start gegangen. Nur Nummern, die seitdem aufgerufen wurden, werden angezeigt.')}}</p>

</div></div>

% include('views/footer.tpl')


