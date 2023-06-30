import React, {useState, useEffect, Fragment} from 'react'
import {connect} from 'react-redux'
import SelectGroup from "./SelectGroup";
import {
  add_task,
} from '../../../redux/actions/admin/tasks'
import {
  get_all_students,
  get_sorted_students,
} from '../../../redux/actions/admin/students'

const AddTask = ({user, sorted_list, get_all_students, get_sorted_students, add_task}) => {
  const [active, setActive] = useState(false)
  const [selectedGroup, setSelectedGroup] = useState(null)
  const [selectedStudents, setSelectedStudents] = useState([])
  const [taskName, setTaskName] = useState('')
  const [taskDescription, setTaskDescription] = useState('')
  const [taskFile, setTaskFile] = useState(null)

  useEffect(() => {
    get_all_students()
  }, [])

  const handleSubmit = e => {
    e.preventDefault()
    const task = {
      teacher: user.id,
      training_group: selectedGroup,
      students: selectedStudents.join(' '),
      name: taskName,
      description: taskDescription,
      file: taskFile,
    }
    setActive(false)
    add_task(task)
    setSelectedGroup(null)
    setSelectedStudents([])
    setTaskName('')
    setTaskDescription('')
    setTaskFile(null)
  }

  const handleCancel = () => {
    setActive(false)
    setSelectedGroup(null)
    setSelectedStudents([])
    setTaskName('')
    setTaskDescription('')
    setTaskFile(null)
  }

  const handleGroupsSelect = data => {
    setSelectedGroup(data)
    get_sorted_students(data)
  }

  const handleStudentsSelect = e => {
    setSelectedStudents([...e.target.options].filter(o => o.selected).map(o => o.value))
  }


  return (
    <>

      <div
        className={`modal fade ${active ? 'show' : ''}`}
        style={{ display: active ? 'block' : 'none' }}
      >
        <div className='modal-dialog'>
          <div className='modal-content'>
            <form onSubmit={handleSubmit}>
              <div className='modal-header'>
                <h4 className='modal-title'>Добавить задание</h4>
                <button
                  type='button'
                  className='close'
                  onClick={handleCancel}
                  aria-hidden='true'
                >
                  &times;
                </button>
              </div>
              <div className='modal-body'>
                <div className='custom-modal-form'>
                  <SelectGroup action={handleGroupsSelect}/>
                  <div className='form-group'>
                    <select
                      multiple
                      className='form-select multiselect'
                      aria-label='Выберите слушателей'
                      onChange={handleStudentsSelect}
                    >
                      <option defaultValue>Выберите слушателей</option>
                      {sorted_list &&
                        sorted_list.map(item => (
                          <option key={item.id} value={item.id}>
                            {item.name}
                          </option>
                        ))}
                    </select>
                  </div>
                  <div className='form-group'>
                    <label>Название</label>
                    <input
                      type='text'
                      className='form-control'
                      value={taskName}
                      onChange={e => setTaskName(e.target.value)}
                    />
                  </div>
                  <div className='form-group'>
                    <label>Описание</label>
                    <textarea
                      className='form-control'
                      value={taskDescription}
                      onChange={e => setTaskDescription(e.target.value)}
                    />
                  </div>
                  <div className='form-group'>
                    <label>Файл</label>
                    <input
                      type='file'
                      className='form-control'
                      onChange={e => setTaskFile(e.target.files[0])}
                    />
                  </div>
                </div>
              </div>
              <div className='modal-footer'>
                <input
                  type='button'
                  className='btn btn-default'
                  value='Отменить'
                  onClick={() => handleCancel()}
                />
                <input
                  type='submit'
                  className='btn btn-info'
                  value='Сохранить'
                />
              </div>
            </form>
          </div>
        </div>
      </div>

      <button
        className='btn btn-success'
        onClick={() => setActive(true)}
      >
        <i className='material-icons'>&#xE147;</i>{' '}
        <span>Добавить задание</span>
      </button>
    </>
  )
}

const mapStateToProps = state => ({
  sorted_list: state.students.sorted_list,
})

export default connect(mapStateToProps, {
  get_all_students,
  get_sorted_students,
  add_task,
})(AddTask)
