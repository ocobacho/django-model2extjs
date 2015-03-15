Ext.application({
    requires: [ 
        'Ext.container.Viewport',
        'Ext.layout.container.Accordion',
    ],
    controllers: [
        'Djmodel'
    ],
    appFolder: '/static/model2extjs/js/app',
    name: 'Ocgenerator',
    launch: function() {
    Ext.create('Ext.container.Viewport', {
            layout: 'border',
            items: [ 
                {
                    xtype: 'tabpanel',
                    title: 'Django-model2extjs | ocobacho@gmx.com',
                    region: 'center',
                    tools: [{
                        type: 'help',
                        handler: function(){
                            Ext.Msg.show({
                               title:'Short Example',
                               msg: "<ol><li>Enter your Extjs app name.</li><li>Click load models (The list of models from your django project should appear).</li><li>Download generated files from the list or double click on the models for selecting and copying the code. </li></ol>",
                               buttons: Ext.Msg.OK,
                               icon: Ext.Msg.QUESTION
                           });
                        }
                    }],
                    layout: 'fit',
                    items: [{
                            title: 'All Models',
                            itemId: 'modelall',
                            xtype: 'djmodellist'
                        },{
                            title: 'About',
                            xtype: 'component',
                            style:"p {padding:10px;}",
                            html: "<h1>About model2extjs</h1><p>Model2extjs is a simple Django app for generating Extjs code (grids, forms and models) from Django models.</p>&copy; Osvaldo Cobacho Aguilera | <a href='mailto:ocobacho@gmx.com'>ocobacho@gmx.com</a>"
                        }]
                }]
        })
    }
});
