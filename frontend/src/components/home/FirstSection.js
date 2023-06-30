import React, {useState, Fragment, useEffect} from 'react';
import {MDBCol, MDBContainer, MDBIcon, MDBIframe, MDBModal, MDBModalBody, MDBModalHeader, MDBRow} from "mdbreact";
import play from '../../assets/play.svg';
import background from '../../assets/home_background4-inv.jpg'
import banner from '../../assets/subsidia.jpg'

import {connect} from 'react-redux';

const FirstSection = ({height, margin}) => {

  const [firstSectionStyle, setFirstSectionStyle] = useState(null)
  const [w, setW] = useState('')
  const [h, setH] = useState('')

  useEffect(() => {
    if(window.innerWidth < 992) {
      setW('384')
      setH('216')
    } else {
      setW('640')
      setH('360')
    }
    let h = window.innerWidth < 992 ? height+60 : height
    let m = window.innerWidth < 992 ? margin : margin+40
    setFirstSectionStyle({height: h, marginTop: m})
  }, [height, margin])

  useEffect(() => {
    let h = window.innerWidth < 992 ? height+60 : height
    let m = window.innerWidth < 992 ? margin : margin+40
    setFirstSectionStyle({height: h, marginTop: m})
  }, [height, margin])

  // const firstSectionStyle = {height: height+40, marginTop: margin}

  const [modal, setModal] = useState(false)

  const toggle = () => {
    setModal(!modal)
  }

  console.log(margin)

  return (
    <Fragment>
      <MDBModal size="auto" isOpen={modal} toggle={toggle} className={'modal-video'}>
        <MDBModalBody className="mb-0 py-0 fluid-modal">
          <button type="button" className="modal-close close" aria-label="Close" onClick={toggle}><span aria-hidden="true">×</span></button>
          <iframe width={w} height={h} src="https://www.youtube.com/embed/XuoNzzWXvPY"
                    title="YouTube video player" frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowFullScreen/>
          {/*<div className="embed-responsive-16by9 z-depth-1-half">*/}
          {/*  */}
          {/*  /!*<MDBIframe src="https://www.youtube.com/embed/XuoNzzWXvPY"/>*!/*/}
          {/*</div>*/}
        </MDBModalBody>
      </MDBModal>
      <div className="d-flex flex-column" style={firstSectionStyle}>
        {/* <a href="/events/8" style={{width:'100%'}}>
          <img src={banner} height="120" style={{width:'100%'}} alt="banner"/>
        </a> */}
      <MDBRow className="w-100 mx-0 d-flex justify-content-stretch idab-2" style={{flex:'1 0 auto'}}>
        <MDBCol className="home-first-section d-flex justify-content-center align-items-center text-idab" md="6">
          <div>
            <h2>Почему я выбрал MBA</h2>
            <p
              style={{cursor: 'pointer'}}
              onClick={toggle}>
              <span className="mr-3">
                <img src={play} alt=""/>
              </span>Смотреть видео отзыв
              наших выпускников
            </p>
          </div>
        </MDBCol>
        <MDBCol
          md="6"
          className="home-first-section"
          style={{ backgroundImage: 'url(' + background + ')', backgroundPosition: 'center', backgroundSize: 'cover'}}
        >
        </MDBCol>
      </MDBRow>
      </div>
    </Fragment>
  )
}
const mapStateToProps = state => ({
  height: state.home.section_height,
  margin: state.home.navbar_height,
});

export default connect(mapStateToProps,)(FirstSection);