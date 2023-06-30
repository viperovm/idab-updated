import {
  GET_ABOUT_MANAGEMENT_SUCCESS,
  GET_ABOUT_MANAGEMENT_FAIL,
  GET_ABOUT_TEACHERS_SUCCESS,
  GET_ABOUT_TEACHERS_FAIL,
  GET_ABOUT_LEADER_SUCCESS,
  GET_ABOUT_LEADER_FAIL,
  GET_ABOUT_GALLERY_SUCCESS,
  GET_ABOUT_GALLERY_FAIL,
  GET_ABOUT_HISTORY_SUCCESS,
  GET_ABOUT_HISTORY_FAIL,
  GET_ABOUT_RATING_SUCCESS,
  GET_ABOUT_RATING_FAIL,
} from '../actions/types'

const initialState = {
  about_leader: {},
  about_management: [],
  about_teachers: [],
  about_gallery: [],
  about_history: [],
  about_rating: [],
};

export default function(state= initialState, action) {
  const {type, payload} = action;

  switch(type) {
    case GET_ABOUT_MANAGEMENT_SUCCESS:
      return {
        ...state,
        about_management: payload.about_management
      }
    case GET_ABOUT_MANAGEMENT_FAIL:
      return {
        ...state,
        about_management: []
      }
      case GET_ABOUT_LEADER_SUCCESS:
      return {
        ...state,
        about_leader: payload.about_leader
      }
    case GET_ABOUT_LEADER_FAIL:
      return {
        ...state,
        about_leader: {}
      }
    case GET_ABOUT_TEACHERS_SUCCESS:
      return {
        ...state,
        about_teachers: payload.about_teachers
      }
    case GET_ABOUT_TEACHERS_FAIL:
      return {
        ...state,
        about_teachers: []
      }
    case GET_ABOUT_GALLERY_SUCCESS:
      return {
        ...state,
        about_gallery: payload.about_gallery
      }
    case GET_ABOUT_GALLERY_FAIL:
      return {
        ...state,
        about_gallery: []
      }

    case GET_ABOUT_HISTORY_SUCCESS:
      return {
        ...state,
        about_history: payload.about_history
      }
    case GET_ABOUT_HISTORY_FAIL:
      return {
        ...state,
        about_history: []
      }

    case GET_ABOUT_RATING_SUCCESS:
      return {
        ...state,
        about_rating: payload.about_rating
      }
    case GET_ABOUT_RATING_FAIL:
      return {
        ...state,
        about_rating: []
      }
    default:
      return state
  }
}