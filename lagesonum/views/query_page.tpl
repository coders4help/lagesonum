% include('views/header.tpl', active='query')

<div class="container">
      <div class="starter-template">

<p>{{_('Willst du wissen, ob deine Nummer am LAGeSo angezeigt wurde? Gib sie hier ein, um es herauszufinden.')}}</p>


<form action="{{i18n_path('/query')}}" method="post" class="form-inline" style="margin-bottom:20px;">
  <div class="form-group">
    <label for="numberfield">{{_('Wartenummer')}}</label>
    <input type="text" name="number" class="form-control" placeholder="e.g. A123" id="numberfield">
  </div>
  <button class="btn btn-primary">{{_('Abschicken')}}</button>
</form>



% if result is not None and result!="NewNumber":
  %if invalid_input:
    <div class="alert alert-warning" role="alert">{{_(u'Ung\xfcltige Eingabe. Bitte einen Buchstaben gefolgt von Zahlen ohne Leerzeichen eingeben.')}}</div>
  %else:
    %if len(timestamps) == 0:
      <div class="alert alert-warning" role="alert">{{_('Es tut uns leid, aber diese Nummer wurde seit dem 20.9.15 noch nicht aufgerufen.')}}</div>
    % else:
      <div class="alert alert-success" role="alert">
        {{_(Deine Wartenummer %(number)s wurde auf dem Display am LaGeSo angezeigt.)}}<br><br>

        % if len(timestamps) == 1:
           {{_(Eine Person hat die Nummer <b>{{result}}</b> auf dem Display gesehen und am %(date)s auf dieser Website eingetragen.)}}<br><br>
        % else:
          %{{_((amount)s Personen haben deine Wartenummer auf dem Display am LaGeSo gesehen und auf dieser Website eingetragen.)}}
        % end

        {{_(Bitte beachte: Je mehr Personen sie sehen und eintragen, desto größer ist die Sicherheit, dass die Nummer wirklich angezeigt wurde und sich keiner vertippt hat.)}}
      </div>
    % end
  %end




<h3>{{_('Bitte beachten:')}}</h3>
<p>{{_(u'Diese Website ist am 22.9.15 an den Start gegangen. Nur Nummern, die seitdem aufgerufen wurden, werden angezeigt.')}}</p>

</div></div>

% include('views/footer.tpl')


