package api

import "github.com/gin-gonic/gin"
import "net/http"

import "yki/src/gateways/controllers"
import "yki/src/gateways/repositories"

type Request struct {
	Motion bool `json:"motion"`
}

func Liten() {
	router := gin.Default()

	// Simple group: v1
	v1 := router.Group("/v1")
	{
		v1.POST("/motions", postMotions)
	}

	router.Run(":8080")
}

func postMotions(c *gin.Context) {
	// TODO:: FactoryMethodで生成リポジトリを変更する
	// mrepo := repositories.NewInMemoryMotionRepository()
	// TODO:: 環境変数からPROJECT_IDを取得する
	mrepo := repositories.NewFirestoreMotionRepository("ca-camp-rabbit-team-2019-12")
	mc := controllers.NewMotionController(mrepo)
	req := load(c)
	m := mc.ConverToMotion(req.Motion)
	mc.Update(m)
	c.JSON(http.StatusOK, mc.MotionToHTTPResponse(mc.Get()))
}

func load(c *gin.Context) Request{
	var req Request
	c.BindJSON(&req)
	return req
}
