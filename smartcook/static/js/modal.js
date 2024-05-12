function modal(url){
  $('.modalcont').load(url, function(){
  })
}


function unload(){
  $('.modalcont').empty()
}
