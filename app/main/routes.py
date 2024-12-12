from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import main
from ..models import Reservation
from .. import db
from ..forms import ReservationForm

# Home route
@main.route('/')
def index():
    return render_template('index.html')

# Reservation route (requires login)
@main.route('/reserve', methods=['GET', 'POST'])
@login_required
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = Reservation(
            name=form.name.data,
            email=form.email.data,
            date=form.date.data,
            time=form.time.data,
            party_size=form.party_size.data
        )
        db.session.add(reservation)
        db.session.commit()
        flash('Your reservation has been made!', 'success')
        return redirect(url_for('main.index'))
    return render_template('reservation_form.html', form=form)

# Admin route to view all reservations
@main.route('/admin')
@login_required
def admin():
    reservations = Reservation.query.all()
    return render_template('admin.html', reservations=reservations)
