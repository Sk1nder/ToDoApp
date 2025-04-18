from datetime import datetime, UTC
from flask import render_template, redirect, url_for, request
from flask_login import current_user
from flask_login import login_required

from ToDoAPP import db
from ToDoAPP.tasks import tasks_bp
from ToDoAPP.forms import ToDoForm, EditForm
from ToDoAPP.models import Task



# add_task route with appropriate comments and validation
@tasks_bp.route('/add_task', methods=["GET", "POST"])
def add_task():
    if not current_user.is_authenticated:
        return render_template("add.html", is_auth=False, current_user=current_user)
    form = ToDoForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Task(
                title=form.titleField.data,
                description=form.descriptionField.data,
                startDate=datetime.now(UTC),
                deadline=datetime.strptime(form.deadlineField.data.strftime("%d-%m-%Y %H:%M"), "%d-%m-%Y %H:%M"),
                author_id=current_user.get_id(),
                endDate=None
            )
        else:
            return render_template("add.html", form=form, is_auth=True, current_user=current_user)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template("add.html", form=form, is_auth=True, current_user=current_user)



# to_do_list route for displaying tasks
@tasks_bp.route('/to_do_list', methods=["GET", "POST"])
@login_required
def to_do_list():
    result = db.session.execute(db.select(Task).where((Task.author_id == current_user.id) & (Task.status == False)))
    tasks = result.scalars().all()
    return render_template("to_do_list.html", tasks=tasks, current_user=current_user)

# to_do_list route for displaying all tasks
@tasks_bp.route('/all_tasks', methods=["GET"])
@login_required
def all_tasks():
    result = db.session.execute(db.select(Task).where(Task.author_id == current_user.id))
    tasks = result.scalars().all()
    return render_template("all_tasks.html", tasks=tasks, current_user=current_user)

# get_status route for getting status from page
@tasks_bp.route('/get_status', methods=['POST'])
@login_required
def get_status():
    result = db.session.execute(db.select(Task).where(Task.author_id == current_user.id))
    tasks = result.scalars().all()
    for task in tasks:
        if str(task.id) in request.form:
            task.status = True
            task.endDate = datetime.now(UTC)
            db.session.commit()
    return redirect(url_for('tasks.to_do_list'))

# finished_tasks route for display finished tasks
@tasks_bp.route('/finished_tasks', methods=["GET", "POST"])
@login_required
def finished_tasks():
    result = db.session.execute(db.select(Task).where((Task.author_id == current_user.id) & (Task.status == True)))
    tasks = result.scalars().all()
    return render_template("finished_tasks.html", tasks=tasks, current_user=current_user)

# edit_task route for editing tasks
@tasks_bp.route('/edit/<int:task_id>', methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = db.get_or_404(Task, task_id)
    edit_form = EditForm(
        titleField=task.title,
        descriptionField=task.description,
        startField=task.startDate,
        endField=task.endDate,
        deadlineField=task.deadline
    )
    if edit_form.validate_on_submit():
        task.title = edit_form.titleField.data
        task.description = edit_form.descriptionField.data
        task.deadline = datetime.strptime(edit_form.deadlineField.data.strftime("%d-%m-%Y %H:%M"), "%d-%m-%Y %H:%M")
        print(edit_form.endField.data)
        if edit_form.endField.data:
            task.endDate = datetime.strptime(edit_form.endField.data.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
        else:
            task.endDate = None
        print(task.endDate)
        task.startDate = datetime.strptime(edit_form.startField.data.strftime("%d-%m-%Y %H:%M"), "%d-%m-%Y %H:%M")
        if request.form.get('checkbox') == None:
            task.status = False
        else:
            task.status = True
        db.session.commit()
        return redirect(url_for('tasks.all_tasks'))
    return render_template("edit_task.html", form=edit_form, task=task, current_user=current_user)

