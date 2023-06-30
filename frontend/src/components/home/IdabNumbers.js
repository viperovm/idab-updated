import React, {useEffect, useState} from 'react';
import background from '../../assets/faces.jpg'

const IdabNumbers = () => {

  const [number, setNumber] = useState(null)
  const [year, setYear] = useState('')

  useEffect(() => {
    setNumber(Number(new Date().getFullYear())-2002)
  }, [])

  useEffect(() => {
    if(number) {
      let str = `${number ? number.toString() : ''}`
      if(
        str[1] === '0' ||
        str[1] === '5' ||
        str[1] === '6' ||
        str[1] === '7' ||
        str[1] === '8' ||
        str[1] === '9'
      ) {
        setYear('Лет')
      } else if(str[1] === '1') {
        setYear('Год')
      } else if(
        str[1] === '2' ||
        str[1] === '3' ||
        str[1] === '4'
      ) {
        setYear('Года')
      }
    }
  }, [number])

  return (
    <div>
      <div className="streak streak-photo streak-long-2" style={{backgroundImage: 'url(' + background + ')'}}>
        <div className="mask flex-center rgba-black-strong">
          <div className="container">
            <h3 className="text-center text-idab-2 mb-5 text-uppercase font-weight-bold wow fadeIn">ИДАБ В ЦИФРАХ</h3>
            <div className="row text-white text-center wow fadeIn">

              <div className="col-md-3 mb-2">
                <p className="h1 text-idab-3 mb-1 font-weight-bold">{number}</p>
                <p className='text-idab-2'>{`${year} на рынке`}</p>
              </div>

              <div className="col-md-3 mb-2">
                <p className="h1 text-idab-3 mb-1 font-weight-bold">11520</p>
                <p className='text-idab-2'>Профессионалов подготовлено</p>
              </div>

              <div className="col-md-3 mb-2">
                <p className="h1 text-idab-3 mb-1 font-weight-bold">36</p>
                <p className='text-idab-2'>Отраслей экономики</p>
              </div>

              <div className="col-md-3 mb-2">
                <p className="h1 text-idab-3 mb-1 font-weight-bold">32</p>
                <p className='text-idab-2'>Средний возраст</p>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default IdabNumbers;