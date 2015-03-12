Ext.define('Ocgenerator.controller.Djmodel', {
    extend: 'Ext.app.Controller',
    stores: ['djmodels'],
    models: ['djmodel'],
    views: ['djmodel.list', 'djmodel.window'],
    refs: [
        { 'ref': 'appname', selector: '#app-name'},
        { 'ref': 'modelname', selector: '#model-name'},
    ],
    init: function() {
        this.control({
        'djmodellist':{
            itemdblclick:function (grid, record) {
                var view = Ext.widget('djmodelwindow'),
                    form = view.down('form');
                form.loadRecord(record);   
            }
        },
        'djmodellist button[action=generate]':{
            click: function (button) {
                console.log(this.getAppname());
                if(this.getAppname().value){
                    this.getStore('djmodels').proxy.extraParams = {
                        'appname': this.getAppname().value,
                        'model_name': this.getModelname().value
                    };
                    if (this.getModelname().value != "") {
                        this.getStore('djmodels').loadPage(1);
                    }else{
                        this.getStore('djmodels').load();
                    }
                }else{
                    Ext.Msg.alert("Message", "Enter your app name");
                }
            }
        },
    });
    },
});