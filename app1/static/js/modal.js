function modal(url){
  $('.modalcont').load(url, function(){
    $(this).modal('show');
  })
}


function unload(){
  $('.modalcont').empty()
}