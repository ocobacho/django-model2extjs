Ext.define('Ocgenerator.store.djmodels', {
    extend: 'Ext.data.Store',
    model: 'Ocgenerator.model.djmodel',
    pageSize: 20,
    //autoLoad: true,
    proxy: {
        type: 'ajax',
        api: {
           read: 'models',
        },
        reader: {
            type: 'json',
            root: 'data',
            totalProperty: 'total',
            //successProperty: 'success'
        },
        actionMethods: {
            read: 'GET',
        },
   },
});
