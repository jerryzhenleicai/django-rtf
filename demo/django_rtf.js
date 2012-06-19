
function FCKeditor_OnComplete(editor ){
  editor.Events.AttachEvent('OnAfterLinkedFieldUpdate', function() {
    editor.LinkedField.style.display = '';
    var frmId = editor.Name  + '___Frame';
    var frm = document.getElementById(frmId);
    frm.style.display = 'none';
  }) ;
}

function toRich(textarea) {
  var editor = new FCKeditor(textarea.name ) ;
  editor.MinWidth = textarea.offsetWidth;
  editor.Width = "100%" ;
  editor.MinHeight = Math.max(textarea.offsetHeight, 200 ) ;
  editor.MaxHeight = 400;
  editor.ToolbarSet = "Zanbato";
  var frmId = textarea.name + '___Frame';
  editor.ReplaceTextarea();
  textarea.style.display = 'none';
}

