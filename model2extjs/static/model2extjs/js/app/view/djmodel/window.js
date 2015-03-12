Ext.define('Ocgenerator.view.djmodel.window', {
	extend: 'Ext.window.Window',
	alias: 'widget.djmodelwindow',
	title: 'Extjs code',
	autoShow: true,
	modal: true,
	initComponent: function() {
		this.items = [{
			xtype: 'form',
			items:[{
				xtype: 'textfield',
				margin: 5,
				name: 'name',
				fieldLabel: 'Django model name',
				labelWidth: '100%',
				readOnly: true
			},{	
				xtype: 'panel',
				title: 'Code',
				border: false,
				width: Ext.themeName === 'neptune' ? 650 : 600,
        		height: Ext.themeName === 'neptune' ? 500 : 440,
				layout: 'accordion',
				items: [{
					title: 'Model code',
					items: [{
						xtype: 'textareafield',
						name: 'model',
						title: 'Model code',
						height: 280,
						readOnly: true,
						width: '100%'
					}]
				},{
					title: 'Grid code',
					items: [{
						xtype: 'textareafield',
						title: 'Grid code',
						name: 'grid',
						height: 280,
						readOnly: true,
						width: '100%'
					}]
				},{
					title: 'Form code',
					items: [{
						xtype: 'textareafield',
						title: 'Form code',
						name: 'form',
						height: 280,
						readOnly: true,
						width: '100%',
					}]
				}],
			}]
		}];
		this.callParent(arguments);
	}
});