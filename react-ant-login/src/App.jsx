import "./App.css";
import React from 'react';
import { Button, Checkbox, Form, Input, Flex } from 'antd';
const onFinish = (values) => {
  console.log('Success:', values);
};
const onFinishFailed = (errorInfo) => {
  console.log('Failed:', errorInfo);
};
const App = () => (
  <Flex
  style={{
    width:'100%',
    height:'100vh',
    justifyContent:"center",
    alignItems:"center"
  }}
  >
    <Form
    name="basic"
   
    style={{
      backgroundColor:'white',
      padding:'1rem',
      borderRadius:'10px',
      display:"flex",
      flexDirection:'column',
      justifyContent:'center',
      alignItems:'center',
      width:"40%",
      gap:"10px",
      boxShadow:"0px 0px 4px #2121"

    }}
    initialValues={{
      remember: true,
    }}
    onFinish={onFinish}
    onFinishFailed={onFinishFailed}
    autoComplete="off"
  >
    <p
    style={{
      fontSize:'200%',
      alignSelf:'start'
    }}
    >
      SignIn
    </p>
    <Form.Item
      label="Username"
      name="username"
      rules={[
        {
          required: true,
          message: 'Please input your username!',
        },
      ]}
      style={{
        width:"90%",
        paddingLeft:"1rem",
      }}
    >
      <Input />
    </Form.Item>

    <Form.Item
      label="Password"
      name="password"
      rules={[
        {
          required: true,
          message: 'Please input your password!',
        },
      ]}
      style={{
        width:"90%",
        paddingLeft:"1rem"
      }}
    >
      <Input.Password />
    </Form.Item>

    

    <Form.Item
      style={{
        width:"90%"
      }}
    >
      <Button
      style={{
        width:"100%"
      }}
       type="primary" htmlType="submit">
        Login
      </Button>
    </Form.Item>
  </Form>
  </Flex>
  
);
export default App;
