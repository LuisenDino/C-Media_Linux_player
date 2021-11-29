window.api = {
    _createApi: function(controllerList){
        for (var i = 0; i < controllerList.length; i++){
            var methodsList = controllerList[i].methods
            var controller = controllerList[i].controller
            window.api[controller] = {}
            window.api.returnValues[controller] = {}
            for (var j = 0; j < methodsList.length; j++){
                var funcName = methodsList[j].func;
                var params = methodsList[j].params

                var funcBody = 
                    "var id = (Math.random()+'').substring(2);"+
                    "var promise = new Promise(function(resolve, reject){"+
                        "window.api._checkValue('"+funcName+"', '"+controller+"',resolve, reject, id);"+
                    "});"+
                    "window.api._bride.call('"+funcName+"', '"+controller+"', arguments, id);"+
                    "return promise"
                
                window.api[controller][funcName] = new Function(params, funcBody)
                window.api.returnValues[controller][funcName] = {}
            }
        }
    },

    _bridge:{
        call: function (funcName, controller , params, id){
            return window.external.call(funcName, controller, JSON.stringify(params), id);
        }
    },

    _checkValue: function(funcName, controller, resolve, reject, id){
        var check = setInterval(function(){
            var returnObj = window.api.returnValues[controller][funcName][id];
            if(returnObj){
                var value = returnObj.value;
                var isError = returnObj.isError;

                delete window.api.returnValues[controller][funcName][id];
                clearInterval(check);
                
                if (isError){
                    var pyError = JSON.parse(value);
                    var error = new Error(pyError.message);
                    
                    reject(error);
                } else {
                    resolve(JSON.parse(value));
                }
            }
        }, 100)
    }, 

    returnValues: {}
}