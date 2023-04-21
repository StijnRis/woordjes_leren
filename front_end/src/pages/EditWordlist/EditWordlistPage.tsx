import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import style from "./ErrorPage.module.css";

interface Props {
  code: number;
}

function EditWordListPage() {
  // Get id
  const params = useParams();
  const id = params.id;
}

export default EditWordListPage;
