Ext.define('Ocgenerator.view.djmodel.list', {
   extend: 'Ext.grid.Panel',
   alias: 'widget.djmodellist',
   title: 'Models',
   store: 'djmodels',
   layout: {
       type: 'auto',
   },
   overflowX: true,
   initComponent: function() {
       this.columns = [
           //{header: 'id', dataIndex: 'id',  flex: 0.2},
           {header: 'name', dataIndex: 'name',  flex: 0.1},
           {header: 'Download', xtype: 'templatecolumn', 
            tpl:'<a href="{modellink}">{name}.js</a>, <a href="{formlink}">{name}form.js</a>, <a href="{gridlink}">grid.js</a>',flex: 0.3},
           {header: 'model', dataIndex: 'model',  flex: 0.2},
           {header: 'grid', dataIndex: 'grid',  flex: 0.2},
           {header: 'form', dataIndex: 'form',  flex: 0.2},


       ];
       this.callParent(arguments);
   },
   dockedItems: [{
        xtype: 'toolbar',
        store: 'nodes',   // same store GridPanel is using
        dock: 'top',
        items: [{
          xtype:'textfield',
          fieldLabel: ' Enter Extjs App name',
          labelWidth: 150,
          itemId: 'app-name'
        },{
          xtype:'textfield',
          fieldLabel: 'Filter by model name',
          labelWidth: 150,
          itemId: 'model-name'
        },{
          xtype: 'button',
          action: 'generate',
          text: 'Load models'
        }]  
    }, {
        xtype: 'pagingtoolbar',
        store: 'djmodels',   // same store GridPanel is using
        dock: 'bottom',  
    },]
});