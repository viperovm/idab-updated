import React from "react";
import {Redirect, Route, Switch} from 'react-router-dom';

import ProgramsSection from "../components/programs/ProgramsSection";
import ProgramsLayout from "../hocs/ProgramsLayout";
import CategorySection from "../components/programs/CategorySection";
import ProgramSection from "../components/programs/ProgramSection";
import Page404 from "./Page404";

const Programs = () => {

  return (
    <ProgramsLayout>
        <Switch>
          <Route exact path='/index.php/programmy/:category_slug/:program_slug' component={ProgramSection}/>
          <Route exact path='/index.php/programmy/:category_slug' component={CategorySection}/>
          <Route exact path='/index.php/programmy' component={ProgramsSection}/>
          <Route exact>
            {<Redirect to="/404"/>}
          </Route>
        </Switch>
      </ProgramsLayout>
  );
}

export default Programs;
