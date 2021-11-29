window.api = {
    _createApi: function(controllerList){
      for(var i = 0; i < controllerList.length; i++){
        var methodList = controllerList[i].methods;
        var controller = controllerList[i].controller; 
        window.api[controller] = {}; 
        window.api.returnValues[controller] = {}; 
        for(var j = 0; j < methodList.length; j++){
          var funcName = methodList[j].func; 
          var params = methodList[j].params; 
          window.api[controller][funcName] = function(params){
            console.log(params)
          }
        }
      };
    }, returnValues: {}
  }
