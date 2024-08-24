from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.main.forms import URLForm
from app.main.models import ScrapedURL
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return render_template('main/index.html')

@main_bp.route('/matches')
@login_required
def matches():
    return render_template('main/matches.html')

@main_bp.route('/add-url', methods=['GET', 'POST'])
@login_required
def add_url():
    form = URLForm()
    if form.validate_on_submit():
        new_url = form.url.data.strip()
        if not new_url:
            flash('URL cannot be empty!', 'warning')
        else:
            # Normalize URL by removing common schemes
            new_url = new_url.lower()
            if new_url.startswith(('http://', 'https://')):
                new_url = new_url.split('//', 1)[1]
            
            # Remove trailing slashes and normalize
            new_url = new_url.rstrip('/')

            # Check for duplicates
            existing_url = ScrapedURL.query.filter_by(url=new_url).first()
            if existing_url:
                flash('URL already exists!', 'warning')
            else:
                scraped_url = ScrapedURL(url=new_url)
                try:
                    db.session.add(scraped_url)
                    db.session.commit()
                    flash('URL added successfully!', 'success')
                except Exception as e:
                    db.session.rollback()
                    flash(f'An error occurred: {str(e)}', 'danger')
                return redirect(url_for('main.add_url'))
    return render_template('main/add_url.html', form=form)

@main_bp.route('/view-urls')
@login_required
def view_urls():
    urls = ScrapedURL.query.all()
    return render_template('main/view_urls.html', urls=urls)
