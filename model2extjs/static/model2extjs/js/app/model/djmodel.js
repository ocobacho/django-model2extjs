Ext.define('Ocgenerator.model.djmodel', {
    extend: 'Ext.data.Model',
    idProperty: 'id',
    fields: ['id', 'name', 'model','modellink', 'formlink', 'gridlink', 'applink', 'grid', 'form'],
});