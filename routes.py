from flask import Blueprint, render_template, request, redirect, url_for, send_file, flash
from .forms import AnalysisForm
from .models import perform_analysis, generate_report
import os

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = AnalysisForm()
    if form.validate_on_submit():
        method = form.method.data
        # Simulate data input for analysis
        data = {'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [0, 1, 0]}
        results = perform_analysis(method, data)
        flash(f'Analysis using {method} completed successfully.', 'success')
        return render_template('index.html', form=form, results=results)
    return render_template('index.html', form=form)

@bp.route('/download/report', methods=['GET', 'POST'])
def download_report():
    data = {'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [0, 1, 0]}
    report_path = generate_report(data)
    return send_file(report_path, as_attachment=True)
