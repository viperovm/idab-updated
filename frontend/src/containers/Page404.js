import React, {useEffect} from 'react';
import {connect} from 'react-redux';
import {resetError} from "../redux/actions/programs";

const Page404 = ({location, resetError}) => {

  useEffect(() => {
    resetError()
  }, [])

  return (
    <>
      <div className="error-container">
        <div className="error text-center">
          <h1>404</h1>
          <h2>ОЙ! СТРАНИЦА НЕ НАЙДЕНА</h2>
          <p className="mb-50">Мы сожалеем, но страница, которую Вы ищете, не существует, была удалена, или временно недоступна.</p>
          <a className="error-btn" href="/">На Главную</a>
        </div>
      </div>
    </>
  );
};

const mapStateToProps = state => ({})
const mapDispatchToProps = {resetError,}

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(Page404)