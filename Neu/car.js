class Car {
  constructor(x, y, width, height) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;

    this.speed = 0;
    this.accerlation = 0.2;
    this.maxspeed = 3;
    this.friction = 0.05;

    this.controls = new Controls();
  }
  update() {
    if (this.controls.forward) {
      this.speed += this.accerlation;
    }
    if (this.controls.reverse) {
      this.speed -= this.accerlation;
    }
    if (this.speed > this.maxspeed) {
      this.speed = this.maxspeed;
    }
    if (this.speed < -this.maxspeed / 2) {
      this.speed = -this.maxspeed / 2;
    }
    if (this.speed > 0) {
      this.speed -= this.friction;
    }
    if (this.speed < 0) {
      this.speed += this.friction;
    }
    if (Math.abs(this.speed) < this.friction) {
      this.speed = 0;
    }
    this.y -= this.speed;

    if (this.controls.left) {
      this.x -= 2;
    }
    if (this.controls.right) {
      this.x += 2;
    }
  }
  draw(ctx) {
    ctx.beginPath();
    ctx.rect(
      this.x - this.width / 2,
      this.y - this.height / 2,
      this.width,
      this.height
    );
    ctx.fill();
  }
}
