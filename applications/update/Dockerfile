FROM golang:1.13-alpine as builder
WORKDIR /go/src
COPY . /go/src
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root
COPY --from=builder /go/src/app .
COPY --from=builder /go/src/ca-camp-rabbit-team-2019-12-firebase-adminsdk-pack4-ff94ef4b4f.json .
ENV GOOGLE_APPLICATION_CREDENTIALS=./ca-camp-rabbit-team-2019-12-firebase-adminsdk-pack4-ff94ef4b4f.json
EXPOSE 8080
CMD ["./app"]
