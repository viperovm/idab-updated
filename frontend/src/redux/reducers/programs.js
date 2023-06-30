import {
  GET_CATEGORIES_SUCCESS,
  GET_CATEGORIES_FAIL,
  GET_CATEGORY_SUCCESS,
  GET_CATEGORY_FAIL, GET_PROGRAM_FAIL, RESET_ERROR,
} from '../actions/types'

const initialState = {
  categories: [],
  category: {},
  error: false,
};

export default function(state= initialState, action) {
  const {type, payload} = action;

  switch(type) {
    case GET_CATEGORIES_SUCCESS:
      return {
        ...state,
        categories: payload.categories
      }
    case GET_CATEGORIES_FAIL:
      return {
        ...state,
        categories: {}
      }
    case GET_CATEGORY_SUCCESS:
      return {
        ...state,
        category: payload.category
      }
    case GET_CATEGORY_FAIL:
    case GET_PROGRAM_FAIL:
      return {
        ...state,
        category: {},
        error: true,
      }

    case RESET_ERROR:
      return {
        ...state,
        error: false,
      }
    default:
      return state
  }
}