@app.route('/dronepage')
def dronepage():

    person = {'name':"NULL", 'secret':"removedthis"}
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    template = '''%s!''' % person['name']
    if session.get('logged_in') is None:
        return render_template('login.html', person=template)

    else:
        flash(u'Drone Package ControlPanel', 'success')

        return render_template("table.html")
