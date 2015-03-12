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
                    layout: 'fit',
                    items: [{
                            title: 'All Models',
                            itemId: 'modelall',
                            xtype: 'djmodellist'
                        },]
                }]
        })
    }
});
