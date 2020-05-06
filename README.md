# django-translator
Word by word translation in your beautiful website.
Process:
  1. You can use this "word-break='true'" in your html.For ex.
  ```<p word-break='true'>Pargraphs</p>. <!--You can use this any text in your website.--!>```
  # In views.py
  ```
  from django.views.decorators.csrf import csrf_exempt 
  @csrf_exempt(I am ignoring the csrf token)
  def trans(request):
    translator = Translator()
    text = request.POST['text']
    dest = request.POST['lang']
    print(dest)
    transText = translator.translate(text, dest=dest)
    print(transText.text)
    return HttpResponse(transText.text)
  ```
# In urls.py
```
 path('get/',trans)
``` 
 
# In app.js
```
  var a = $("[word-break='true']");
  var total_dom = a.length;

  for (i=0;i<total_dom;i++){
      let text = a[i].innerHTML.split(' ');
      let spans = text.map(n=>{
          return `<span> ${n} </span>`
      }).join('');
      $(a[i]).html(spans)
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
```
