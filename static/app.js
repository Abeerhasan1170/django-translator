var language = prompt("Shortcode of your native language(english->en,korean->ko,bengali->bn,hindi->hi)");


var a = $("[word-break='true']");
var total_dom = a.length;

for (i=0;i<total_dom;i++){
    let text = a[i].innerHTML.split(' ');
    let spans = text.map(n=>{
        return `<span> ${n} </span>`
    }).join('');
    $(a[i]).html(spans)
}



function getData() {
    return new Promise(resolve => 'success');
  }


$('span').click(function(){
    var t = [];
    var token = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url:'get/',
        method: 'POST',
        data:{
            text:this.textContent,
            lang:language,
            csrfmiddlewaretoken:token

        },
       success:(e)=>{
            if (e.length>0){
                this.textContent = ' '+e;
            }
            
        },
        
    });




});






  